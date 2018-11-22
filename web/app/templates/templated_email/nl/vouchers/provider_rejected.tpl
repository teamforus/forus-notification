
{% extends "templated_email/base.tpl" %}
{% block subject %}Uw aanmelding voor een fonds.{% endblock %}
{% block html %}
    Beste {{ provider_name }},
    <br/>
    <br/>
    Kort geleden heeft u zich aangemeld voor {{ fund_name }}.
    <br/>
    {{ sponsor_name }} heeft uw aanmelding afgewezen.
    <br/>
    <br/>
    Wilt u hiervan de reden weten? Neem dan contact op met {{ sponsor_name }}.
    <br/>
    <br/>
    Met vriendelijke groet,
    <br/>
    <br/>
    {{ sponsor_name }}
{% endblock %}
