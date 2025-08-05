FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /app

RUN pip install -r requirements_bot.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80" ]