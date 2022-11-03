from django.contrib import admin
from .models import Profile, ProfilePhoto



class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'address', 'city')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(ProfilePhoto)
