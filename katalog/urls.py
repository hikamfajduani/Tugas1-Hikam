# TODO: Implement Routings Here
from django.urls import path
from katalog.views import show_katalog, show_wishlist

app_name = 'katalog'

urlpatterns = [
    path('', show_katalog, name='show_katalog'),
]