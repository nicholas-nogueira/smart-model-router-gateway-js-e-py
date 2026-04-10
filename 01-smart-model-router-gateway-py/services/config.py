import os
from dotenv import load_dotenv
from dataclasses import dataclass
from typing import TypedDict


load_dotenv()

class ProviderSort(TypedDict):
    by: str
    partition: str


class ProviderConfig(TypedDict):
    sort: ProviderSort


@dataclass(frozen=True)
class ModelConfig:
    api_key: str
    http_referer: str
    x_title: str
    models: list[str]
    port: int
    temperature: float
    max_tokens: int
    system_prompt: str
    provider: ProviderConfig


def load_config() -> ModelConfig:
    api_key = os.getenv("OPENROUTER_API_KEY")
    assert api_key, "OPENROUTER_API_KEY is not set"
    return ModelConfig(
        api_key=api_key,
        http_referer="https://teste.com",
        x_title="Teste OpenRouter",
        port=3000,
        models=[
            'anthropic/claude-sonnet-4.5',
            'openai/gpt-5-mini',
            'google/gemini-3-flash-preview',
        ],
        temperature=0.2,
        max_tokens=20000,
        system_prompt="You are a helpful assistant.",
        provider={
            "sort": {
                #"by": "latency",
                #"by": "throughput",
                "by": "price",
                "partition": "none"
            }
        },
    )
