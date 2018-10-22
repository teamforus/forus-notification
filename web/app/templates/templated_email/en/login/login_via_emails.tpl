
{% extends "templated_email/base.tpl" %}
{% block subject %}Your login details{% endblock %}
{% block html %}
Dear citizen,

You’ve just requested to login on to the webshop.
Click on the link below to continue logging in.
    <br/>
    <a href="{{ link }}">Link</a>
{% endblock %}