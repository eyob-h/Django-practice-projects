from django.contrib import admin
from .models import User, UserProfile
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(UserAdmin):
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    ordering = ('-date_joined',) #don't forget the comma
    list_display = ['first_name','last_name','email', 'role', 'is_active']  

# class UserAdmin(admin.ModelAdmin):
#     fields = ['first_name','last_name','email', 'role']


admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile)