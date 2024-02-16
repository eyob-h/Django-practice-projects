from django.urls import path 
from . import views

urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
    path('markAsCompleted/<int:pk>', views.markAsCompleted, name='markAsCompleted'),
    path('deleteTask/<int:pk>', views.deleteTask, name='deleteTask'),
    path('editTask/<int:pk>', views.editTask, name='editTask'),
    path('updateTask/<int:pk>', views.updateTask, name='updateTask'),
]