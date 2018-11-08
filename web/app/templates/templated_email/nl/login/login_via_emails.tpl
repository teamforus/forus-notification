
{% extends "templated_email/base.tpl" %}
{% block subject %}Jouw inloggegevens{% endblock %}
{% block html %}
    Beste inwoner,
    <br/>
    Je hebt zojuist aangegeven dat je wil inloggen op de {{ platform }}.
    <br/>
    <br/>
    Klik op onderstaande <a href="{{ link }}" target="_blank" style="color: #315efd; text-decoration: underline;">link</a> om verder te gaan met inloggen.
    <br/>
    <a href="{{ link }}" target="_blank" style="color: #315efd; text-decoration: underline;">{{ link }}</a>
{% endblock %}

