from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from cabshare.users.forms import UserChangeForm, UserCreationForm

User = get_user_model()

class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User

class UserAdmin(UserAdmin):

    form = MyUserChangeForm
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('phone_number',)}),
    )
    list_display = ["username", "name", "is_superuser"]
    search_fields = ["name"]

admin.site.register(User, UserAdmin)