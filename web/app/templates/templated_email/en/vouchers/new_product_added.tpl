
{% extends "templated_email/base.tpl" %}
{% block subject %}A new product or service has been added to the webshop{% endblock %}
{% block html %}
Dear {{sponsor_name }}, <br/>

A new product or service has been added to the webshop. <br/>
View the webshop to check if it meets the requirements to be purchased from {{ fund_name }}.
{% endblock %}