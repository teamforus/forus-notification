from django.contrib import admin


# Register your models here.
from apps.notification_user.models import User, UserConnectionField

admin.site.register(User)
admin.site.register(UserConnectionField)

