
{% extends "templated_email/base.tpl" %}
{% block subject %}A new fund is added{% endblock %}
{% block html %}
  Dear citizen,

    A new fund is added. Your organisation meets the requirements to apply for {{ fund_name }}.
Please log in to the provider dashboard to apply for this fund.


    <br/>
    <a href="{{ provider_dashboard_link }}">{{ provider_dashboard_link }}</a>
{% endblock %}