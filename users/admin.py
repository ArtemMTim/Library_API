from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "patronymic",
        "birth_date",
        "address",
        "phone_number",
        "email",
        "tg_id",
        "avatar",
    )
    search_fields = ("email", "first_name", "last_name", "phone_number", "tg_id")
    list_filter = ("email", "first_name", "last_name", "phone_number", "tg_id")
