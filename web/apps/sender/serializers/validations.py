from rest_framework import serializers

from apps.sender.serializers import BaseSerializer


class SponsorAddYouAsValidatorSerializer(BaseSerializer):
    sponsore_name = serializers.CharField()
    validator_name = serializers.CharField()

    def get_template(self):
        return '/validations/you_added_as_validator'


class NewValidationRequestSerializer(BaseSerializer):
    validator_name = serializers.CharField()

    def get_template(self):
        return '/validations/new_validation_request'
