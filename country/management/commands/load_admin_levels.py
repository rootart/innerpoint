import json

from django.contrib.gis.geos import GEOSGeometry
from django.core.management.base import BaseCommand

from country.models import AdminLevelEntry, Country


class Command(BaseCommand):
    help = "Load admin level data for the country"

    def add_arguments(self, parser):
        parser.add_argument('source', type=str, nargs='?')

    def handle(self, *args, **options):
        source_filepath = options.get('source')
        data = json.loads(open(source_filepath, 'r').read())

        for item in data['features']:
            entries = AdminLevelEntry.objects.filter(
                osm_id=item['id']
            )
            if entries.exists():
                continue

            country = Country.objects.all().first()
            geometry = GEOSGeometry(
                json.dumps(item.get('geometry'))
            )
            entry = AdminLevelEntry(
                country=country,
                osm_id=item['id'],
                osm_type=item.get('osm_type'),
                name=item.get('name', ''),
                properties=item.get('properties'),
                admin_level=item.get('properties', {}).get('admin_level'),
                geometry=geometry
            )
            entry.save()
