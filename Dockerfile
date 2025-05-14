# Используем базовый образ Python
FROM python:3.12-slim

# Устанавливаем рабочую директорию
WORKDIR /app


#RUN apt-get update && \
#    apt-get install -y --no-install-recommends gcc

## Копируем файл зависимостей и устанавливаем их
COPY requirements.txt .
#
RUN pip install -r requirements.txt
#
## Копируем исходный код приложения в контейнер

COPY . .

RUN python admin.py