
{% extends "templated_email/base.tpl" %}
{% block subject %}Aanbieding QR-code gedeeld door {{ requester_email }}{% endblock %}
{% block title %}Aanbieding QR-code gedeeld door {{ requester_email }}{% endblock %}
{% block html %}
    {{ product_name }}<br />
    <img style="display: block; margin: 0 auto;" src="{{ qr_url }}" width="300" />
    <br />
    {{ requester_email }} heeft deze QR-code met u gedeeld met het volgende bericht:<br />
    {{ reason }}
{% endblock %}
