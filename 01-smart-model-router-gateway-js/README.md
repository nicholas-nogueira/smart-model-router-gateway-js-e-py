# Projeto
Smart router gateway com OpenRouter
- Escolher automaticamente uma LLM de acordo com o preço ou tempo de resposta

## Stacks
- Typescript sem usar transpilador (usar Typescript nativamente no JS, com Intellicense melhor sem usar outras libs)

## Requisitos
- Node v24

### 1. Iniciar node
``` bash
npm init -y
```

### 2. Instalar melhor api node.js
```bash 
npm i fastify@5.7.4 @types/node@24
```

### 3. Adicionar script `dev` no package.json e alterar `type` para `module`
```json 
  "scripts": {
    "dev": "node --inspect --watch src/index.ts",
  },
  "type": "module"
```
- inspect: para usar debugger
- watch: atualiza servidor na tela ao editar arquivos (live reload)

Para rodar no modo `debugger` acessar aba `Run and Debug` e clicar em `JavaScript Debug Terminal`. Irá abrir um novo terminal do tipo 'debug'. Agora poderá usar breakpoints e ver logs no terminal com consolo.log.

### 4. Criar arquivo tsconfig.json

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ESNext",
    "lib": [
      "ES2022"
    ],
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "noEmit": true,
    "esModuleInterop": true,
    "forceConsistentCasingInFileNames": true,
    "strict": true,
    "skipLibCheck": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "allowSyntheticDefaultImports": true,
    "types": [
      "node"
    ]
  },
  "exclude": [
    "node_modules",
    "dist"
  ]
}
```

Para o servidor aplicar as configurações desse novo arquvio dar o comando `ctrl + shift + p` => `Typescript` => `Restart TS Server`


### 5. Instalar OpenRouter SDK 

```bash
npm install @openrouter/sdk@0.5.1
```

### 6. Configurar para obter o .env ao rodar a aplicação em `dev`

```json
  "scripts": {
    "dev": "node --env-file .env --inspect --watch src/index.ts",
    "test": "echo \"Error: no test specified\" && exit 1"
  }
```


### 7. Criar pasta e arquivo de teste `test/router.test.ts`

### 8. Adicionar os scripts de teste

```json
  "scripts": {
    "dev": "node --env-file .env --inspect --watch src/index.ts",
    "test:dev": "node --env-file .env --inspect --watch --test ./test/**/*.test.ts",
    "test": "node --env-file .env --test ./test/**/*.test.ts"
  }
```
