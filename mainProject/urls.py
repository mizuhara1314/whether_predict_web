
from django.contrib import admin
from django.urls import path
from firstWEB import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('current', views.current),
    path('provinces', views.provinces),
    path('cities_search', views.cities_search),
    path('cities_result', views.cities_result),
    path('places_search', views.places_search),
    path('places_result', views.places_result),
    path('forecast', views.forecast),
]
