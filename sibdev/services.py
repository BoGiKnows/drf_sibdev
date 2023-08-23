from datetime import datetime

from rest_framework import status

from sibdev.models import Gem, Deals, Client


def parse_data(data):
    Deals.objects.all().delete()
    if not data:
        return "Status: Error, Desc: Прикрепите файл - в процессе обработки файла произошла ошибка.", status.HTTP_400_BAD_REQUEST

    if data.name.split('.')[-1] != 'csv':
        return "Status: Error, Desc: Файл должен быть в формате .csv - в процессе обработки файла произошла ошибка.", status.HTTP_415_UNSUPPORTED_MEDIA_TYPE

    lines = list(map(lambda x: x.decode('utf-8'), data.file.readlines()))
    try:
        for line in lines[1:]:
            customer, item, total, quantity, date = line.split(',')
            date = datetime.strptime(date.strip(), '%Y-%m-%d %H:%M:%S.%f').astimezone()
            gem, _ = Gem.objects.get_or_create(title=item)
            customer, _ = Client.objects.get_or_create(username=customer)
            customer.gems.add(gem)
            Deals.objects.get_or_create(customer=customer, item=gem, total=total, quantity=quantity, date=date)
    except ValueError:
        return "Status: Error, Desc: Структура файла не соответствует формату - в процессе обработки файла произошла ошибка.", status.HTTP_422_UNPROCESSABLE_ENTITY

    return 'Status: OK - Файл был обработан без ошибок', status.HTTP_204_NO_CONTENT

