from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import (
    TestModel,
    OccupantModel,
    BodyZoneModel,
    PresetZonesModel,
    GlobalResponseModel,
    LocalResponseModel,
    ProfileModel
)

# Register
admin.site.register([
    TestModel,
    OccupantModel,
    BodyZoneModel,
    PresetZonesModel,
    GlobalResponseModel,
    LocalResponseModel
])

# Add user profile to user
class ProfileInline(admin.StackedInline):
    model = ProfileModel
    can_delete = False
    verbose_name_plural = 'profile'
# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
