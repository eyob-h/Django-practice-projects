from django.urls import path
from . import views

urlpatterns = [
    path('',  views.view_listings, name='view_listings'),
    path('create/', views.create_listing, name='create'),
    path('<pk>/', views.view_single_listing, name='view_single_listing'),
    
    
    # IT DOESN'T WORK IN THIS ORDER
    # path('create/', views.create_listing, name='create'),
    # path('<pk>/', views.view_single_listing, name='view_single_listing'),


]