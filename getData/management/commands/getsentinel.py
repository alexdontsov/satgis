# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
# from main_app import models


class Command(BaseCommand):
    # Задаём текст помощи, который будет
    # отображён при выполнении команды
    # python manage.py createtags --help
    help = 'Creates specified number of tags'

    # def add_arguments(self, parser):


        # В данном случае, это один аргумент типа int.
        # parser.add_argument('tags_count', nargs=1, type=int)

    def handle(self, *args, **options):
        # Получаем аргумент, создаём необходимое количество тегов
        # и выводим сообщение об успешном завершении генерирования
        # tags_count = options['tags_count'][0]
        #
        # for i in range(tags_count):
        #     models.Tag.objects.create(text='Tag{0}'.format(i))
        #
        # self.stdout.write('Successfully created {0} tags!'.format(tags_count))
        print 'aaaaaaaa'