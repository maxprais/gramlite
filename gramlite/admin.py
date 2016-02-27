from django.contrib import admin
from .models import User, Image

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'user_id')

class ImageAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'image_link')
    search_fields = ['user_id']

admin.site.register(User, UserAdmin)
admin.site.register(Image, ImageAdmin)
