
{% extends "templated_email/base.tpl" %}
{% block subject %}Jouw inloggegevens{% endblock %}
{% block html %}
Beste inwoner,

Je hebt zojuist aangegeven dat je wil inloggen op de {{ platform }}.
Klik op onderstaande <a href="{{ link }}">link</a> om verder te gaan met inloggen.

    <br/>
    <a href="{{ link }}">{{ link }}</a>
{% endblock %}

