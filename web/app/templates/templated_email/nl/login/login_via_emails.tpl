
{% extends "templated_email/base.tpl" %}
{% block subject %}Jouw inloggegevens{% endblock %}
{% block html %}
Beste inwoner,

Je hebt zojuist aangegeven dat je wil inloggen op de webshop.
Klik op onderstaande link om verder te gaan met inloggen.

    <br/>
    <a href="{{ link }}">Link</a>
{% endblock %}