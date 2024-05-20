from django.contrib import admin
from .models import Profile, SavedPost


@admin.register(SavedPost)
class SavedAdmin(admin.ModelAdmin):
    list_display = ['post']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'avatar']