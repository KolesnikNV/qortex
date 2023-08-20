# Qortex API

Это API предоставляет каталог исполнителей и их альбомов с песнями.

## Установка

1. Склонируйте репозиторий: ```git clone https://github.com/KolesnikNV/qortex.git```

2. Перейдите в папку проекта: ```cd qortex```

3. Используйте poetry ```poetry install``` или pip ```pip install -r requirements.txt``` для установки зависимостей 

4. Запустите сервер локально: ```python manage.py runserver``` 

5. Можно запустить используя Docker: ```docker-compose build ``` - для сборки контейнера и ```docker-compose up ``` - для запуска контейнера  

## API Endpoints

- `GET /api/artists/` - Список исполнителей
- `GET /api/albums/` - Список альбомов
- `GET /api/songs/` - Список песен

## Swagger API Documentation

Документация API доступна через Swagger UI:
- `http://localhost:8000/swagger/`
