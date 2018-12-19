
{% extends "templated_email/base.tpl" %}
{% block subject %}Your fund has reached your balance limit{% endblock %}
{% block title %}Your fund has reached your balance limit{% endblock %}
{% block button_link %}{{ sponsor_dashboard_link }}{% endblock %}
{% block html %}
    Dear {{sponsor_name}},
    <br/>
    <br/>
    The balance on your '{{fund_name}}' has reached the limit of €{{treshold_amount}}.
    Login to the sponsor dashboard to increase the balance.
    <br/>
    <a href="{{ sponsor_dashboard_link }}" target="_blank" style="color: #315efd; text-decoration: underline;">{{ sponsor_dashboard_link }}</a>

{% endblock %}