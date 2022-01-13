from django.contrib import admin, auth
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import UserChangeForms, UserCreationForms

# Register your models here.
@admin.register(User)
class UserAdmin(UserAdmin):
    form = UserChangeForms
    add_form = UserCreationForms
    model = User
    fieldsets = UserAdmin.fieldsets + (
        ("campos personalizados",{"fields":("bio",)}),
    )
