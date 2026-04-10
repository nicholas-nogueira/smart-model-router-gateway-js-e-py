import {createServer} from './server.ts';
import { config } from './config.ts';
import { OpenRouterService } from './openRouterService.ts';

const openRouterService = new OpenRouterService(config);
const app = createServer(openRouterService);

await app.listen({ port: 3000, host: '0.0.0.0' }); 
console.log('Server is running on port 3000');
/*
app.inject({ 
    method: 'POST',
    url: '/chat',
    body: {
        question: 'What is the capital of France?'
    }
}).then((response) => {
    console.log('Response status code', response.statusCode);
    console.log('Response body', response.body);
}).catch((error) => {
    console.error('Error injecting request: ', error);
});
*/