
{% extends "templated_email/base.tpl" %}
{% block subject %} {{fund_name}} is van start gegaan{% endblock %}
{% block title %} {{fund_name}} is van start gegaan{% endblock %}
{% block html %}
    Dear provider,
    <br/>
    <br/>
    You have recently been approved by {{sponsor_name}} to participate in the {{fund_name}}.
    <br/>
    As of today, this fund is active. This means that from today on you can expect customers who want to use their {{fund_name}}-voucher.
    <br/>

{% endblock %}
