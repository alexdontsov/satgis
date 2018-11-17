# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from getData.Sentinel import getSentinelData


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
            '--waterObject', dest='waterObject', required=True,
            help='waterObject id...',
        )
        parser.add_argument(
            '--date_start', dest='date_start', required=False,
            help='Date start...',
        )
        parser.add_argument(
            '--date_stop', dest='date_stop', required=False,
            help='Date stop...',
        )
        parser.add_argument(
            '--platformname', dest='platformname', required=True,
            help='platformname...',
        )
        parser.add_argument(
            '--cloud', dest='cloud', required=False,
            help='cloud...',
        )

    def handle(self, *args, **options):
        # get arguments
        date = options['date']
        endDate = options['date_stop']
        geojson = options['geojson']
        waterObject = options['waterObject']
        platformname = options['platformname']

        getSentinelData(geojson, waterObject, date, endDate, platformname)
