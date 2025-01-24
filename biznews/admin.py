from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Post, Category, Comment  # Assuming your User model is in the same app



class CustomUserAdmin(UserAdmin):
    model = User

    # Add avatar to the list_display to show it in the user list
    list_display = ['username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'avatar_preview']

    # Add avatar field to the fieldsets to make it editable in the user form
    fieldsets = (
        ('User Information', {'fields': ('username', 'email', 'first_name', 'last_name', 'password', 'avatar', 'bio', 'hobbies', 'experience', 'phone', 'social')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Add avatar to the add_fieldsets for the user creation form
    add_fieldsets = (
        ('User Information', {'fields': ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'avatar')}),
    )

    # Function to display a preview of the avatar in the user list
    def avatar_preview(self, obj):
        if obj.avatar:
            return f'<img src="{obj.avatar.url}" width="50" height="50" />'
        return 'No avatar'
    avatar_preview.allow_tags = True  # Allows HTML to be rendered in the admin

    # Restrict Editors to only their own profile
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs  # Superusers can see all users
        if request.user.groups.filter(name='Editor').exists():  # Check if user is in the Editor group
            return qs.filter(id=request.user.id)  # Only show the logged-in editor's profile
        return qs

    # Optionally, you can restrict Editors from adding or deleting users
    def has_add_permission(self, request):
        # Optionally disable adding new users for editors
        return False

    def has_delete_permission(self, request, obj=None):
        # Optionally disable deleting users for editors
        return False



# class EditorAdmin(admin.ModelAdmin):
#     list_display = ['name', 'user', 'position', 'email', 'total_views']
#     search_fields = ['name', 'user__username', 'position']


# Register the CustomUserAdmin class
admin.site.register(User, CustomUserAdmin)

# Register other models
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
# admin.site.register(Editor, EditorAdmin)
