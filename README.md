# drf_sibdev
Тестовое задание 


Установка и запуск проекта:
- docker-compose up

Ендпоинты:
GET
- http://localhost:8000/api/v1/get-top/
  Получение 5 покупателей с самым большим суммами на покупку
  пример запроса:
  curl --location 'http://127.0.0.1:8000/api/v1/get-top/'
  
POST
- http://127.0.0.1:8000/api/v1/post-deals/
  В тело запроса прикрепляем файл c ключом "deals"
  пример запроса:
  curl --location 'http://127.0.0.1:8000/api/v1/post-deals/' \
  --form 'deals=@"/F:/PycharmProjects/DJANGO/drf_sibdev/deals.csv"'
