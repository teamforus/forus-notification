from rest_framework import serializers

from apps.sender.serializers import BaseEmailSerializer


class SponsorAddYouAsValidatorEmailSerializer(BaseEmailSerializer):
    sponsore_name = serializers.CharField()

    def get_template(self):
        return '/validations/you_added_as_validator'


class NewValidationRequestEmailSerializer(BaseEmailSerializer):
    validator_dashboard_link = serializers.CharField()

    def get_template(self):
        return '/validations/new_validation_request'
