from django.contrib.gis import admin  # type: ignore


from .models import Country, AdminLevelEntry


class CountryAdmin(admin.GeoModelAdmin):  # type: ignore
    pass


class AdminLevelEntryAdmin(admin.GeoModelAdmin):
    list_filter = ('admin_level', )


admin.site.register(AdminLevelEntry, AdminLevelEntryAdmin)
admin.site.register(Country, CountryAdmin)  # type: ignore
