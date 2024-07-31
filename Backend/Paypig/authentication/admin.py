from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
class CustomAdmin(UserAdmin):
    model = CustomUser
    fieldsets = (
        (None, {'fields': ('email', 'password', 'price')}),
        ("Permissions", {"fields": ('is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ("email", "password", "password2", "price")
            }
        ),
    )
    list_display = ("email", "is_active", "is_staff", "is_superuser")
    search_fields = ("email",)
    ordering = ("email",)
    exclude = ('first_name', 'last_name','username')


admin.site.register(CustomUser,CustomAdmin)