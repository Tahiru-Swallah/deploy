from django.contrib import admin
from .models import CustomUser, Code

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'phone_number', 'is_active', 'is_staff']

@admin.register(Code)
class CodeAdmin(admin.ModelAdmin):
    list_display = ['number', 'user']