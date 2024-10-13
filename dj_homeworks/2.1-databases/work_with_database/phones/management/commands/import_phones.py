import csv
from datetime import date
from slugify import slugify

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            phone_obj = Phone(id=phone['id'],
                              name=phone['name'],
                              price=int(phone['price']),
                              image=phone['image'],
                              release_date=date.fromisoformat(
                                  phone['release_date']),
                              lte_exists=bool(phone['lte_exists']),
                              slug=slugify(phone['name'])
                              )
            phone_obj.save()
            # TODO: Добавьте сохранение модели
