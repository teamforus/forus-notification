
{% extends "templated_email/base.tpl" %}
{% block subject %}A new fund is added{% endblock %}
{% block html %}
    Dear citizen,
    <br/>
    A new fund has been created. You are eligible to participate in {{ fund_name }}.
    <br/>
    <br/>
    Go to <a href="{{ webshop_link }}" target="_blank" style="color: #315efd; text-decoration: underline;">{{webshop_link}}</a>, log in to the webshop to sign up for {{ fund_name }}.
{% endblock %}