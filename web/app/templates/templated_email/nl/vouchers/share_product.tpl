
{% extends "templated_email/base.tpl" %}
{% block subject %}Aanbieding QR-code gedeeld door {{ requester_email }}{% endblock %}
{% block title %}Aanbieding QR-code gedeeld door {{% endblock %}
{% block html %}
    {{ product_name }}<br />
    <img style="display: block; margin: 0 auto;" src="{{ qr_url }}" width="300" />
    <br />
    {{ requester_email }} heeft deze qr-code met u gedeeld met de volgende informatie:<br />
    {{ reason }}
{% endblock %}
