from . import views
from django.urls import path

# Routes are defined here
# Don't need .as_view() function as these are already views
urlpatterns = [
    path('', views.translator_view, name = 'translator_view')
]
