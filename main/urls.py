from . import views
from django.urls import path

urlpatterns = [
    path('birthdays', views.get_birthdays, name="get_birthdays"),
    path('import_artists/', views.import_artists, name='import_artists'),
]
