console.assert(process.env.OPENROUTER_API_KEY, 'OPENROUTER_API_KEY is not set');

export type ModelConfig = {
    apiKey: string;
    httpReferer: string;
    xTitle: string;
    models: string[];
    port: number;
    temperature: number;
    maxTokens: number;
    systemPrompt: string;
    provider: {
     sort: {
         by: string;
         partition: string;
     }
    }
 }
 
export const config: ModelConfig = {
    apiKey: process.env.OPENROUTER_API_KEY!,
    httpReferer: "https://teste.com",
    xTitle: "Teste OpenRouter",
    port: 3000,
    models: [
        'anthropic/claude-sonnet-4.5',
        'openai/gpt-5-mini',
        'google/gemini-3-flash-preview',
    ],
    temperature: 0.2,
    maxTokens: 100,
    systemPrompt: "You are a helpful assistant.",
    provider: {
        sort: {
            //by: "latency",
            by: "throughput",
            //by: "price",
            partition: "none"
        }
    }
}