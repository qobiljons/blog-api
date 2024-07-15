from typing import Any

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.db.models.aggregates import Count
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
    list_display = ("first_name", "last_name", "is_staff", "is_superuser")
    ordering = ["first_name", "last_name"]
    search_fields = ("first_name", "last_name", "username")

    

