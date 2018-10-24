
{% extends "templated_email/base.tpl" %}
{% block subject %}  A provider wants to join a fund.{% endblock %}
{% block html %}
Dear {{ sponsor_name }}, <br/>

A registration has been received from a provider to participate in {{ fund_name }}.
    Check whether this {{ provider_name }} meets your conditions to participate. <br/>
    Log in to the sponsor dashboard <a href="{{ sponsor_dashboard_link }}">{{ sponsor_dashboard_link }}</a> to process this registration.
{% endblock %}