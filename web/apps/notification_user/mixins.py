from fcm_django.api.rest_framework import DeviceViewSetMixin

from apps.notification_user.models import UserConnectionField, UserConnectionFCMDevice


class UserConnectionMixin(object):
    def create_connection(self, user_id, type, value):

        user_connection =  UserConnectionField.objects.get_or_create(user_id, type, value)
        
        if type == UserConnectionField.FIREBASE_TYPE:
            fcm_connection = UserConnectionFCMDevice.objects.get_or_create_by_connection(user_connection)


        return user_connection
