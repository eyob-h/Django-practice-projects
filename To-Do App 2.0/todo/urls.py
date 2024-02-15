from django.urls import path 
from . import views

urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
    path('markAsCompleted/<int:pk>', views.markAsCompleted, name='markAsCompleted')
]