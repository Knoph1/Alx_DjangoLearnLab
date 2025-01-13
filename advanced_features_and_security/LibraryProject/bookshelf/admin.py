from django.contrib import admin

# Register your models here.
# bookshelf/admin.py
from django.contrib import admin
from .models import Book

admin.site.register(Book)

# bookshelf/admin.py
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Define fields to display in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add search functionality
    search_fields = ('title', 'author__name')  # Assuming 'author' is a foreign key to an Author model
    
    # Add filters for easy categorization
    list_filter = ('publication_year', 'author')

# Register the Book model with the customized admin class
admin.site.register(Book, BookAdmin)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from myapp.models import Article

def setup_groups():
    content_type = ContentType.objects.get_for_model(Article)

    permissions = {
        "Viewers": ["can_view"],
        "Editors": ["can_view", "can_edit", "can_create"],
        "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
    }

    for group_name, perm_names in permissions.items():
        group, created = Group.objects.get_or_create(name=group_name)
        for perm_name in perm_names:
            permission = Permission.objects.get(codename=perm_name, content_type=content_type)
            group.permissions.add(permission)
