from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from user_account.models import User
from django.contrib.auth.forms import UserChangeForm

from user_account.forms import UserAdminCreationForm, UserChangeForm


User = get_user_model()


class UserAdmin(admin.ModelAdmin):
    search_fields = ["email"]
    # update form
    form = UserChangeForm
    # create form
    add_form = UserAdminCreationForm

    list_display = ("email", "is_admin")
    list_filter = ("is_admin", 'is_staff',)
    fieldsets = (
        (None, {"fields": ("email", "password", "first_name", "last_name")}),
        ("Personal Info", {"fields": ("bio",)}),
        ("Permissions", {"fields": ("is_admin",)}),
    )

    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User)