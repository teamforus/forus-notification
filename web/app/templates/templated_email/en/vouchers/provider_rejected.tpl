
{% extends "templated_email/base.tpl" %}
{% block subject %}{{ product_name }} voucher is no longer valid.{% endblock %}
{% block html %}
    Dear citizen,
    <br/>
    {{ sponsor_name }} has rejected {{ provider_name }} to participate as a provider.
    This means that you can no longer use {{ product_name }} voucher.

    We apologize for the inconvenience.
{% endblock %}