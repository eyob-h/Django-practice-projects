from django.urls import path
from . import views
from accounts import views as AccountViews

urlpatterns = [
    # path('registerVendor/', views.registerVendor, name='registerVendor'),
    path('', AccountViews.venDashboard, name='vendor'),
    path('profile/', views.vprofile, name='vprofile'),
]