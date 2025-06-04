FROM python:3.11-alpine

WORKDIR /app

# Instalar uv
RUN pip install uv

# Copiar todos os arquivos do projeto (incluindo pyproject.toml)
COPY . .

# Instalar dependências usando uv a partir do pyproject.toml no ambiente do sistema
RUN uv pip install . --system

EXPOSE 8080

# Definir a variável de ambiente FLASK_APP
ENV FLASK_APP=src.app

# Rodar a aplicação Flask
CMD ["flask", "run", "--port", "8080", "--host", "0.0.0.0"] 