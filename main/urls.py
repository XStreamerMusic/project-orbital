from . import views
from django.urls import path

urlpatterns = [
    path('birthdays', views.get_birthdays, name="get_birthdays"),
    # path('add-sample-artists/', views.AddSampleArtistsView.as_view(), name='add_sample_artists'),
]
