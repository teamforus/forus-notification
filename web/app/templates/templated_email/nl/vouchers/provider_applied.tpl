
{% extends "templated_email/base.tpl" %}
{% block subject %} {{ provider_name }} wilt zich aanmelden voor {{ fund_name }}{% endblock %}
{% block button_link %}{{ sponsor_dashboard_link }}{% endblock %}
{% block html %}
    Beste {{ sponsor_name }},
    <br/>
    <br/>
    Er is een aanmelding binnengekomen om deel te nemen aan {{ fund_name }}.
    <br/>
    <br/>
    Controleer of {{ provider_name }} voldoet aan uw voorwaarden om deel te nemen.
    <br/>
    Meld u aan op het sponsor dashboard <a href="{{ sponsor_dashboard_link }}" target="_blank" style="color: #315efd; text-decoration: underline;">{{ sponsor_dashboard_link }}</a> om deze aanvraag te behandelen.
{% endblock %}
