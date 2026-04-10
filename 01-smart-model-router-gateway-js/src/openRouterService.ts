import { OpenRouter } from '@openrouter/sdk';
import { config, type ModelConfig } from './config.ts';
import { type ChatGenerationParams } from '@openrouter/sdk/models';

export type LLMResponse = {
    model: string,
    content: string
}

export class OpenRouterService {
    private client: OpenRouter;
    private modelConfig: ModelConfig;

    constructor(configOverride?: ModelConfig) {
        this.modelConfig = configOverride ?? config;
        this.client = new OpenRouter({
            apiKey: this.modelConfig.apiKey,
            httpReferer: this.modelConfig.httpReferer,
            xTitle: this.modelConfig.xTitle,
        });
    }

    async generate(prompt: string) : Promise<LLMResponse> {
        const response = await this.client.chat.send({
            models: this.modelConfig.models,
            messages: [
                { role: 'system', content: this.modelConfig.systemPrompt },
                { role: 'user', content: prompt }
            ],
            stream: false,
            temperature: this.modelConfig.temperature,
            maxTokens: this.modelConfig.maxTokens,
            provider: this.modelConfig.provider as ChatGenerationParams['provider']
        })

        const content = String(response.choices.at(0)?.message.content) ?? 'No content';

        return {
            model: response.model,
            content: content
        }

    }

}