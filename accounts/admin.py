from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser



class CustomUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('bio', 'profile_picture','pk')
    model = CustomUser
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("bio", "profile_picture",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("bio", "profile_picture",)}),
    )
admin.site.register(CustomUser, CustomUserAdmin)