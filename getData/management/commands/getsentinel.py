# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
# from main_app import models


class Command(BaseCommand):

    help = 'Download Sentinel data'

    def add_arguments(self, parser):

        parser.add_argument(
            '--date', dest='date', required=True,
            help='Date...',
        )
        parser.add_argument(
            '--geojson', dest='geojson', required=True,
            help='Geojson...',
        )

        parser.add_argument(
            '--date_start', dest='date_start', required=True,
            help='Date start...',
        )
        parser.add_argument(
            '--date_stop', dest='date_stop', required=True,
            help='Date stop...',
        )
        parser.add_argument(
            '--platformname', dest='platformname', required=True,
            help='platformname...',
        )
        parser.add_argument(
            '--cloud', dest='cloud', required=True,
            help='cloud...',
        )

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