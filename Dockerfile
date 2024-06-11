# Determina a base do container
FROM python:3.11

# Atualizações (opcional, se necessário)
RUN apt-get update && apt-get upgrade -y

# Variável de ambiente
ENV PYTHONUNBUFFERED 1

# Diretório onde vai ficar a aplicação dentro do container
WORKDIR /app/project

# Criação e ativação do ambiente virtual, instalação de dependências e cópia do código
COPY requirements.txt ./
RUN python -m venv .venv \
    && /app/project/.venv/bin/pip install --no-cache-dir -r requirements.txt \
    && echo "source .venv/bin/activate" >> ~/.bashrc
COPY . ./

# Comando padrão para iniciar o servidor Django
CMD ["/app/project/.venv/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]
