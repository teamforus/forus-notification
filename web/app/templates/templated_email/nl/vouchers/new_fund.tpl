
{% extends "templated_email/base.tpl" %}
{% block subject %} Er is een nieuw fonds toegevoegd{% endblock %}
{% block html %}
    Beste inwoner,
    <br/>
    Er is een nieuw fonds aangemaakt. U voldoet aan de voorwaarden om mee te doen aan {{fund_name}}. Log in op het leveranciers dashboard om u aan te melden.
    <br/>
    <br/>
    <a href="{{ provider_dashboard_link }}" target="_blank" style="color: #315efd; text-decoration: underline;">{{ provider_dashboard_link }}</a>
{% endblock %}
