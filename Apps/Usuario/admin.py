from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserChangeForms, UserCreationForms
from .models import User


# Register your models here.
@admin.register(User)
class UserAdmin(UserAdmin):  # type: ignore
    form = UserChangeForms
    add_form = UserCreationForms
    model = User
    fieldsets = UserAdmin.fieldsets + (
        ("campos personalizados", {"fields": ("bio",)}),
    )
