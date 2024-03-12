from django.urls import path
from . import views

urlpatterns = [
    path('',  views.view_listings, name='view_listings'),
    path('<pk>/', views.view_single_listing, name='view_single_listing')
]