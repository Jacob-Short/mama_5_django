from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from user_account.models import UserAccount
from django.contrib.auth.forms import UserChangeForm


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