
{% extends "templated_email/base.tpl" %}
{% block subject %}Inloggen op {{ platform }}{% endblock %}
{% block button_text %}Inloggen{% endblock %}
{% block button_link %}{{ link }}{% endblock %}
{% block title %}Log in op {{ platform }}{% endblock %}
{% block header_image %} https://media.forus.io/static/iphone_shield_594x594.png {% endblock %}
{% block html %}
    Beste gebruiker,
    <br/>
    <br/>
    U heeft zojuist aangegeven dat u wilt inloggen op {{ platform }}.
    <br/>
    <br/>
    Klik <a href="{{ link }}" target="_blank" style="color: #315efd; text-decoration: underline;">hier</a> of op de knop hieronder om in te loggen.
    <br/>
{% endblock %}

