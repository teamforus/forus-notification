
{% extends "templated_email/base.tpl" %}
{% block subject %}A new fund is added{% endblock %}
{% block html %}
    Dear citizen,
    <br/>
    A new fund is added. Your organisation meets the requirements to apply for {{ fund_name }}.
    <br/>
    <br/>
    Please log in to the provider dashboard to apply for this fund.
    <br/>
    <a href="{{ provider_dashboard_link }}" target="_blank" style="color: #315efd; text-decoration: underline;">{{ provider_dashboard_link }}</a>
{% endblock %}