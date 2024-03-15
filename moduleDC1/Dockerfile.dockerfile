FROM python:3.12.2

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8

RUN curl -sSL https://install.python-poetry.org | sh
RUN apt-get update && apt-get install -y git

WORKDIR /app
COPY . /app

RUN poetry install

CMD ["python", "Bot.py"]