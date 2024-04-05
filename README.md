# Проект по запуску счетчика робота с выводом в консоль

Робот принимает любое значение и начинает от него отсчет с шагом в 1 каждую секунду
Скрипт робота может быть отдельно запущен. Дефолтное значение отсчета равняется 0

## Что умеет проект:
-Через эндопинт /start можно передать значение начала отсчета
-Через эндпоинт /stop можно остановить отсчет и выключить скрипт

## Запуск проекта

***Клонируйте репозиторий***

git@github.com:Kuvapa/robot_greenatom.git

***Установите и активируйте виртуальное окружение:***

Win:
```
python -m venv venv
venv/Scripts/activate
```
Mac:
```
python3 -m venv venv
source venv/bin/activate
```
***Установите зависимости из файла requirements.txt:***

```pip install -r requirements.txt```

***Создайте файл .env и сохраните в нем PROJECT_NAME(название проекта) и BACKEND_CORS_ORIGINS(адрес, на котором будете запускать проект). Пример заполнения файла:***

```
PROJECT_NAME=robot_greenatom
BACKEND_CORS_ORIGINS=["http://localhost:8000", "https://localhost:8000", "http://localhost", "https://localhost"]
```

***Запуск проекта***

```
uvicorn main:app --reload 
```

[С дальнейшей документацией проекта можно ознакомиться по адресу](https://localhost:8000/docs)