
{% extends "templated_email/base.tpl" %}
{% block subject %}Uw fonds heeft uw ingestelde grens bereikt{% endblock %}
{% block title %}Uw fonds heeft uw ingestelde grens bereikt{% endblock %}
{% block button_link %}{{ sponsor_dashboard_link }}{% endblock %}
{% block html %}
    Beste {{sponsor_name}},
    <br/>
    <br/>
    Het budget op uw fonds '{{fund_name}}' heeft de grens van €{{treshold_amount}} bereikt.
    <br/>
    U kunt inloggen op het sponsor dashboard om uw budget aan te vullen.
    <br/>
    <a href="{{ sponsor_dashboard_link }}" target="_blank" style="color: #315efd; text-decoration: underline;">{{ sponsor_dashboard_link }}</a>

{% endblock %}