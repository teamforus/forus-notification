
{% extends "templated_email/base.tpl" %}
{% block subject %} {{product_name}} has been added to the web-shop{% endblock %}
{% block html %}
  A new product or service has been added to the web-shop by {{provider_name}}
  View the web-shop to check if {{product_name}} meets the requirements to be purchased from the fund.
{% endblock %}