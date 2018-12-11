
{% extends "templated_email/base.tpl" %}
{% block subject %}Email activation{% endblock %}
{% block button_text %}Verify{% endblock %}
{% block button_link %}{{ link }}{% endblock %}
{% block title %}Email activation{% endblock %}
{% block header_image %} https://media.forus.io/static/iphone_shield_594x594.png {% endblock %}
{% block html %}
    You are getting this mail because you entered your email adres on our {{ platform }}. With this mail we verify your e-mailadres.
    <br/>
    <br/>
    Please press this <a style="color: #315efd; text-decoration: underline;" href="{{ link }}" target="blank">link</a> or this button to verify your mail.
    <br/>
{% endblock %}