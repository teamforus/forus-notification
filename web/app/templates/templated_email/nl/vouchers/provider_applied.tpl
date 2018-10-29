
{% extends "templated_email/base.tpl" %}
{% block subject %} {{ provider_name }} wil zich aanmelden voor {{ fund_name }}{% endblock %}
{% block html %}
  Beste {{ sponsor_name }}, <br/>

Er is een aanmelding binnengekomen om deel te nemen aan {{ fund_name }}.
    Controleer of deze {{ provider_name }} voldoet aan je voorwaarden om deel te nemen.<br/>s
    Meld je aan op het sponsor dashboard <a href="{{ sponsor_dashboard_link }}">{{ sponsor_dashboard_link }}</a> om deze aanvraag te behandelen.
{% endblock %}