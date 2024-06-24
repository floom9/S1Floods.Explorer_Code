from django.urls import path
from .views import index, load_geojson, get_dates_for_event, get_all_data

urlpatterns = [
    path('', index, name='index'),
    path('load_geojson/', load_geojson, name='load_geojson'),
    path('get_dates/', get_dates_for_event, name='get_dates'),
    path('get_all_data/', get_all_data, name='get_all_data'),  # New URL pattern

]