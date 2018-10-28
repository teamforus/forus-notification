import django
from rest_framework import serializers


class BaseSerializer(serializers.Serializer):
    reffer_id = serializers.CharField(allow_blank=False, min_length=1)
    # public_key = serializers.CharField(allow_blank=False, min_length=1)
    # sign = serializers.CharField(allow_blank=False, min_length=1)

    def validate(self, attrs):
        self.reffer_id = attrs['reffer_id']
        return attrs


    def get_template(self):
        raise NotImplementedError('Template not implimented')


    def get_lang_template(self):
        return  'templated_email/' + django.utils.translation.get_language() + self.get_template() + '.tpl'


class BaseMobileSerializer(BaseSerializer):
    def get_template(self):
        return ''

    def get_lang_template(self):
        return ''

class BaseEmailSerializer(BaseSerializer):

    reffer_id = serializers.CharField(allow_blank=False, min_length=1)

