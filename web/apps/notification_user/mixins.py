from apps.notification_user.models import UserConnectionField


class UserConnectionMixin(object):
    def create_connection(self, user_id, type, value):
        return UserConnectionField.object.get_or_create(user_id, type, value)