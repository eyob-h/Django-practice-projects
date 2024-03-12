from django.urls import path
from . import views

urlpatterns = [
    path('',  views.view_listings, name='view_listings' )
]