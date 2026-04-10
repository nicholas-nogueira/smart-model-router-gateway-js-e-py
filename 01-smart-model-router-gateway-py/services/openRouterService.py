"""Cliente OpenRouter equivalente a `openRouterService.ts`."""


import asyncio

from openrouter import OpenRouter

from services.config import ModelConfig, load_config


class OpenRouterService:
    def __init__(self, config_override: ModelConfig):
        self._model_config = config_override or load_config()
        self._client = OpenRouter(
            api_key=self._model_config.api_key,
            http_referer=self._model_config.http_referer,
            x_open_router_title=self._model_config.x_title,
        )

    def sendChat(self, prompt: str):
        return self._client.chat.send(
            models=self._model_config.models,
            messages=[
                {"role": "system", "content": self._model_config.system_prompt},
                {"role": "user", "content": prompt},
            ],
            stream=False,
            temperature=self._model_config.temperature,
            max_tokens=self._model_config.max_tokens,
            provider=self._model_config.provider,
        )

    def generate(self, prompt: str) -> dict[str, str]:
        response = self.sendChat(prompt)
        choice = response.choices[0] if response.choices else None
        raw_content = choice.message.content if choice else None
        return {"model": response.model, "content": raw_content}
