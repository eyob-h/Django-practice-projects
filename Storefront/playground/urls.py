from django.urls import path
# from .views import sayHi
from . import views


urlpatterns = [
    path('hi/', views.sayHi)
]

