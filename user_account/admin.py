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

    list_display = ("email", "admin")
    list_filter = ("admin", 'staff', 'is_active')
    fieldsets = (
        (None, {"fields": ("email", "password", "first_name", "last_name")}),
        ("Personal Info", {"fields": ("bio",)}),
        ("Permissions", {"fields": ("admin",)}),
    )

    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User)

# class UserAdmin(BaseUserAdmin):
#   form = UserChangeForm
#   fieldsets = (
#       (None, {'fields': ('email', 'password', )}),
#       (_('Personal info'), {'fields': ('first_name', 'last_name')}),
#       (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
#                                      'groups', 'user_permissions')}),
#       (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
#         (_('user_info'), {'fields': ('picture', 'bio', 'isNew')}),
#   )
#   add_fieldsets = (
#       (None, {
#           'classes': ('wide', ),
#           'fields': ('email', 'password1', 'password2'),
#       }),
#   )
#   list_display = ['email', 'first_name', 'last_name', 'is_staff', "picture", "bio"]
#   search_fields = ('email', 'first_name', 'last_name')
#   ordering = ('email', )
# admin.site.register(UserAccount, UserAdmin)
