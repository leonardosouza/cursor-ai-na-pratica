# Calculator API com Flask e Docker

Este projeto implementa uma API simples para realizar operações matemáticas básicas (adição, subtração, multiplicação e divisão) utilizando o framework web Flask. O projeto é estruturado seguindo boas práticas e inclui uma configuração Docker para facilitar a execução em diferentes ambientes.

## Ideia do Projeto

O objetivo principal deste projeto é criar um serviço de backend leve que oferece funcionalidades de calculadora através de uma API REST. Ele demonstra a criação de rotas, o processamento de requisições POST com dados JSON e o tratamento de erros em uma aplicação Flask básica. A adição de Docker visa mostrar como empacotar a aplicação para implantação.

## Tecnologias Utilizadas

*   **Python:** Linguagem de programação principal.
*   **Flask:** Framework web leve para construir a API.
*   **Flask-CORS:** Extensão para habilitar o Cross-Origin Resource Sharing (CORS), permitindo requisições de frontends hospedados em domínios diferentes.
*   **uv:** Gerenciador de pacotes e ambiente virtual rápido, utilizado para gerenciar as dependências do projeto.
*   **Docker:** Plataforma para desenvolver, enviar e executar aplicações em contêineres.

## Estrutura do Projeto

A aplicação está organizada da seguinte forma:

```
.
├── Dockerfile
├── README.md
├── .dockerignore
├── .gitignore
├── pyproject.toml
├── uv.lock
├── requirements.txt # Gerado a partir do uv.lock/pyproject.toml
└── src/
    ├── __init__.py
    ├── app.py
    └── calculator/
        ├── __init__.py
        ├── api.py
        └── logic.py
```

*   `src/`: Contém o código fonte da aplicação Python.
    *   `src/app.py`: Ponto de entrada da aplicação Flask, registra o Blueprint da calculadora.
    *   `src/calculator/`: Pacote Python para a funcionalidade da calculadora.
        *   `src/calculator/logic.py`: Contém as funções de adição, subtração, multiplicação e divisão.
        *   `src/calculator/api.py`: Define o Blueprint do Flask com a rota `/calculate`.
*   `Dockerfile`: Define como construir a imagem Docker da aplicação.
*   `pyproject.toml`: Arquivo de configuração do projeto e gerenciamento de dependências com `uv`.
*   `uv.lock`: Arquivo de lock gerado pelo `uv` para garantir dependências determinísticas.
*   `requirements.txt`: Arquivo de dependências gerado para compatibilidade (usado no Dockerfile).
*   `.gitignore`: Especifica arquivos e diretórios a serem ignorados pelo Git.
*   `.dockerignore`: Especifica arquivos e diretórios a serem ignorados pelo Docker build.

## Como Executar

Você pode executar a aplicação de duas formas: localmente ou utilizando Docker.

### Execução Local (com uv)

1.  Certifique-se de ter o Python (>=3.11) e o `uv` instalados.
2.  Navegue até o diretório raiz do projeto no seu terminal.
3.  Crie um ambiente virtual e instale as dependências usando `uv`:
    ```bash
    uv venv
    source .venv/bin/activate  # No Linux/macOS
    # .venv\Scripts\activate  # No Windows
    uv sync
    ```
4.  Execute a aplicação Flask como um módulo:
    ```bash
    python -m src.app
    ```
5.  A API estará disponível em `http://127.0.0.1:5000`.

### Execução com Docker

1.  Certifique-se de ter o Docker instalado.
2.  Navegue até o diretório raiz do projeto no seu terminal.
3.  Construa a imagem Docker:
    ```bash
    docker build -t calculadora-api .
    ```
4.  Execute um container a partir da imagem, mapeando a porta 8080:
    ```bash
    docker run -d -p 8080:8080 calculadora-api
    ```
5.  A API estará disponível em `http://127.0.0.1:8080`.

## Como Testar a API (com cURL)

Com a API rodando (localmente na porta 5000 ou com Docker na porta 8080), você pode usar comandos `cURL` para testá-la. Substitua `[PORT]` pela porta correta (5000 ou 8080).

**Adição:**
```bash
curl -X POST \
  http://127.0.0.1:[PORT]/calculate \
  -H 'Content-Type: application/json' \
  -d '{"num1": 10, "num2": 5, "operation": "add"}'
```

**Subtração:**
```bash
curl -X POST \
  http://127.0.0.1:[PORT]/calculate \
  -H 'Content-Type: application/json' \
  -d '{"num1": 10, "num2": 5, "operation": "subtract"}'
```

**Multiplicação:**
```bash
curl -X POST \
  http://127.0.0.1:[PORT]/calculate \
  -H 'Content-Type: application/json' \
  -d '{"num1": 10, "num2": 5, "operation": "multiply"}'
```

**Divisão:**
```bash
curl -X POST \
  http://127.0.0.1:[PORT]/calculate \
  -H 'Content-Type: application/json' \
  -d '{"num1": 10, "num2": 5, "operation": "divide"}'
```

---

Sinta-se à vontade para explorar o código, fazer melhorias ou adicionar novas funcionalidades!
