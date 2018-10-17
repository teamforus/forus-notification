import django
from rest_framework import serializers


class BaseSerializer(serializers.Serializer):

    reffer_id = serializers.CharField(allow_blank=False, min_length=1)

    def get_template(self):
        raise NotImplementedError('Template not implimented')


    def get_lang_template(self):
        return  'templated_email/' + django.utils.translation.get_language() + self.get_template() + '.tpl'

    def validate(self, attrs):
        self.reffer_id = attrs['reffer_id']
        return attrs