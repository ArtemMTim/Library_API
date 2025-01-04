from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "tg_id",
        "first_name",
        "last_name",
        "phone_number",
        "avatar",
    )
    search_fields = ("email", "first_name", "last_name", "phone_number")
    list_filter = ("email", "first_name", "last_name", "phone_number")
