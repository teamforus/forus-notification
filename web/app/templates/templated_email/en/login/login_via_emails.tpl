
{% extends "templated_email/base.tpl" %}
{% block subject %}Your login details{% endblock %}
{% block html %}
    Dear citizen,
    <br/>
    You’ve just requested to login on to the {{ platform }}.
    <br/>
    <br/>
    Click on the <a style="color: #315efd; text-decoration: underline;" href="{{ link }}" target="blank">link</a> below to continue logging in.
    <br/>
    <a href="{{ link }}" target="_blank" style="color: #315efd; text-decoration: underline;">{{ link }}</a>
{% endblock %}