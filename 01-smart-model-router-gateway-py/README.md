# Iniciar projeto com uv

### STEP 1
O `uv` é um gerenciador de pacotes e ambientes Python moderno, rápido e escrito em Rust, feito pela Astral (mesma equipe do Ruff). Ele substitui boa parte do que você fazia com `pip`, `venv`, `pip-tools`, `pipx` etc. em um único binário. [hub.asimov](https://hub.asimov.academy/blog/uv-python/)

Abaixo vai um passo a passo bem prático para começar a usar `uv` com Python.

***

### 1. Instalar o `uv`

No macOS / Linux (mais comum):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

No Windows (PowerShell):

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Depois, reinicie o terminal (ou rode o script de env do `uv`) para ter o comando `uv` disponível. [dio](https://www.dio.me/articles/usar-uv-com-python-dfea182a9990)

***

### 2. Criar um projeto Python com `uv init` na pasta do projeto

```bash
uv init 
```

O `uv init` cria:

- `pyproject.toml`
- `.python-version`
- `.gitignore`
- `main.py` básico

Isso já configura o projeto para usar `uv` como gerenciador. [usandopy](https://www.usandopy.com/bibliotecas-python/uv-simplificando-o-desenvolvimento-em-python-com-um-gerenciador-de-pacotes-tudo-em-um-e-mais-rapido/)

***

### 3. Instalar Python e criar o ambiente virtual

Listar versões disponíveis de Python:

```bash
uv python list
```

Instalar uma versão específica (ex.: 3.11):

```bash
uv python install 3.11
```

Ou deixar o `uv` escolher a versão padrão do projeto:

```bash
uv python install
```

Depois, criar/sincronizar o ambiente virtual:

```bash
uv sync
```

Esse comando lê o `pyproject.toml` e cria (ou atualiza) o `.venv`. [datacamp](https://www.datacamp.com/pt/tutorial/python-uv)

***

### 4. Instalar pacotes

Em vez de `pip install`:

```bash
uv add requests
uv add flake8 black
```

Se quiser instalar dependências de desenvolvimento (dev-only):

```bash
uv add --group dev pytest mypy
```

O `uv` gera automaticamente entradas no `pyproject.toml` e resolve dependências de forma muito rápida. [hub.asimov](https://hub.asimov.academy/blog/uv-python/)

***

### 5. Rodar scripts e o interpretador Python

Para rodar um script usando o Python do ambiente do `uv`:

```bash
uv python main.py
```

Ou apenas abrir o REPL:

```bash
uv python
```

O `uv python` sempre usa o Python do projeto configurado em `.python-version` e do ambiente virtual criado por `uv sync`. [dio](https://www.dio.me/articles/uv-revolucione-seu-gerenciamento-de-projetos-python)

***

### 6. Comandos básicos de gestão

Alguns equivalentes úteis:

| O que você fazia antes       | Com `uv`                          |
|------------------------------|------------------------------------|
| `python -m venv .venv`       | `uv sync`  [dio](https://www.dio.me/articles/usar-uv-com-python-dfea182a9990)                 |
| `pip install package`        | `uv add package`  [hub.asimov](https://hub.asimov.academy/blog/uv-python/)          |
| `pip install -r requirements.txt` | `uv pip sync requirements.txt`  [hub.asimov](https://hub.asimov.academy/blog/uv-python/) |
| `pipx run tool`              | `uv run tool` (ou `uv tool run`)  [dio](https://www.dio.me/articles/uv-revolucione-seu-gerenciamento-de-projetos-python) |

***

Se você quiser, posso montar um exemplo de `pyproject.toml` completo para um projeto típico (API, CLI, etc.) usando só `uv`.

Para instalar um `requirements.txt` quando você está usando `uv`, você tem duas formas comuns, dependendo do que você quer:

***

### 6. Instalar diretamente no ambiente virtual

Se você já tem um ambiente virtual (criado por `uv` ou outro) e só quer instalar o que está no `requirements.txt`:

```bash
uv pip install -r requirements.txt
```

Esse comando é o equivalente a `pip install -r requirements.txt`, mas usando o `pip` integrado ao `uv`. [stackoverflow](https://stackoverflow.com/questions/79344035/how-to-add-requirements-txt-to-uv-environment/79344041)


Não, o ambiente virtual **não fica ativo automaticamente no terminal** só por usar o `uv`, mas o próprio `uv` ajuda a usar o ambiente correto sem precisar ativar na mão toda hora. [hub.asimov](https://hub.asimov.academy/blog/uv-python/)

***

### Quando o ambiente virtual é “ativo”

1. **Comando `uv` sempre usa o ambiente certo**  
   - Comandos como `uv add`, `uv run`, `uv sync` **detectam automaticamente** o `.venv` do projeto e usam esse ambiente. [reddit](https://www.reddit.com/r/learnpython/comments/1md4hyj/i_think_i_have_to_admit_im_confused_by_how_to/)
   - Você não precisa rodar `source .venv/bin/activate` ou `.\.venv\Scripts\activate` antes, o `uv` faz isso internamente.

2. **Terminal “nativo” ainda precisa ser ativado**  
   - Se você rodar `python` ou `pip` direto no terminal, o ambiente **não estará ativo** a menos que você ative o `.venv` manualmente (ou configure o shell para ativar ao entrar na pasta). [fastapi.tiangolo](https://fastapi.tiangolo.com/pt/virtual-environments/)

***

### O que você pode fazer na prática

- Para **instalar pacotes e rodar scripts**: use sempre `uv` (ex.: `uv add`, `uv run script.py`), que já usa o ambiente virtual. [hub.asimov](https://hub.asimov.academy/blog/uv-python/)
- Se quiser ativar o `.venv` no terminal mesmo (para usar `python` direto), rode:  
  - Linux/macOS: `source .venv/bin/activate`  
  - Windows: `.venv\Scripts\activate`  

Se quiser, posso te mostrar como fazer o terminal ativar o `.venv` automaticamente ao entrar na pasta do projeto (com `direnv` ou similar).
