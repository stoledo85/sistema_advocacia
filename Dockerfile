FROM python:3.8
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

#Define o Diretorio do projeto do Usuario.
WORKDIR /home/stoledo/Projetos/sistema_advocacia
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]