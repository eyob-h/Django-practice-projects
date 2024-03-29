from django.urls import path
from . import views
from django.conf.urls import include


urlpatterns = [
    path('', views.myAccount),
    path('registerUser/', views.registerUser, name = 'registerUser'),
    path('registerVendor/', views.registerVendor, name='registerVendor'),
    
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    path('myAccount/', views.myAccount, name='myAccount'),
    path('custDashboard/', views.custDashboard, name='custDashboard'),
    path('venDashboard/', views.venDashboard, name='venDashboard'),

    path('activate/<uidb64>/<token>/',views.activateAccount , name='activate'),

    path('forgot_password/', views.forgotPassword, name='forgotPassword'),
    path('reset_password_validation/<uidb64>/<token>/', views.resetPasswordValidation, name='resetPasswordValidation'),
    path('reset_password/', views.resetPassword, name='resetPassword'),

    path('vendor/', include('vendors.urls') )

    # path('forgot_password/', views.forgot_password, name='forgot_password'),
    # path('reset_password_validate/<uidb64>/<token>/', views.reset_password_validate, name='reset_password_validate'),
    # path('reset_password/', views.reset_password, name='reset_password'),
]