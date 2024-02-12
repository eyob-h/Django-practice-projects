from django.urls import path
# from .views import sayHi
from . import views

#URLconf  url configuration
urlpatterns = [
    path('hi/', views.sayHi)
]

