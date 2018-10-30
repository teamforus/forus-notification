from django.contrib import admin

# Register your models here.
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.notification_user.models import User, UserConnectionField


class UserConnectionFieldResource(resources.ModelResource):
    class Meta:
        model = UserConnectionField


class UserResource(resources.ModelResource):
    class Meta:
        model = User


class UserAdmin(ImportExportModelAdmin):
    resource_class = UserResource


class UserConnectionFieldAdmin(ImportExportModelAdmin):
    resource_class = UserConnectionFieldResource


admin.site.register(User, UserAdmin)
admin.site.register(UserConnectionField, UserConnectionFieldAdmin)
