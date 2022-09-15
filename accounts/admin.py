from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = get_user_model()
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    fieldsets = ((None, {"user info": ("bio", "profile_picture",)}))
    add_fieldsets = ((None, {"user info": ("bio", "profile_picture",)}))
