from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['email', 'name', 'is_staff', 'is_active', 'created_at']
    search_fields = ('email', 'name')
    ordering = ('email',)   

