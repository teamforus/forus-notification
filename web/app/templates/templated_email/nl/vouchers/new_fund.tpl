
{% extends "templated_email/base.tpl" %}
{% block subject %} Er is een nieuw fonds toegevoegd{% endblock %}
{% block html %}
  Geachte {{username}},

Er is een nieuw fonds aangemaakt. Je voldoet aan de voorwaarden om mee te doen aan {{fund_name}}. Log in op het leveranciers dashboard om je aan te melden.


    <br/>
    <a href="{{ provider_dashboard_link }}">{{ provider_dashboard_link }}</a>
{% endblock %}