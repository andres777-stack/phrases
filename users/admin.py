from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

CustomUser = get_user_model()

@admin.register(CustomUser) #aquí el original es user.
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_fieldsets = UserAdmin.add_fieldsets + ( #add_fieldsets es una tupla, con otra tupla anidada. 
        ('Optional Fields', {
            'classes': ('wide',), #La coma para señalar que es una tupla.
            'fields': ('email', 'first_name', 'last_name'),
        }),
    )

# Register your models here.
