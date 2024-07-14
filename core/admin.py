from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.

@admin.register(models.CustomUser)
class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("first_name", "last_name", "email", "username", "password1", "password2"),
            },
        ),
    )   


