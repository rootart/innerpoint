from django.contrib import admin
from django.urls import path
from country.views import RandomCountryPointView

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'api/v1/country/<str:iso_2_digit>/random-point/',
        RandomCountryPointView.as_view(),
        name='api-country-random-point'
    ),
]
