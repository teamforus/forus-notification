
{% extends "templated_email/base.tpl" %}
{% block subject %}Your login details{% endblock %}
{% block button_text %}Login{% endblock %}
{% block button_link %}{{ link }}{% endblock %}
{% block title %}Log in to Me{% endblock %}
{% block header_image %} https://media.forus.io/static/iphone_shield_594x594.png {% endblock %}
{% block html %}
    Dear user,
    <br/>
    You’ve just requested to log in to the{{ platform }}.
    <br/>
    <br/>
    Click <a style="color: #315efd; text-decoration: underline;" href="{{ link }}" target="blank">here</a> or the button below to log in.
    <br/>
{% endblock %}