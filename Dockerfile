# Use uma imagem base do Python
FROM python:latest


WORKDIR /app 

# Copia os arquivos do projeto para o contêiner
COPY . /app

# Cria um ambiente virtual e instala as dependências
RUN python -m venv venv && \
    . venv/bin/activate && \
    pip install -r requirements.txt

# Comando padrão para iniciar a aplicação
CMD ["python", "app.py"]