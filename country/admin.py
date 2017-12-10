from django.contrib.gis import admin  # type: ignore


from .models import Country


class CountryAdmin(admin.GeoModelAdmin):  # type: ignore
    pass


admin.site.register(Country, CountryAdmin)  # type: ignore
