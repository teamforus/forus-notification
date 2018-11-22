
{% extends "templated_email/base.tpl" %}
{% block subject %}Uw aanmelding voor {{fund_name}}{% endblock %}
{% block html %}
    Uw aanmelding is geaccepteerd!
    <br/>
    <br/>
    Beste {{ provider_name }},
    <br/>
    <br/>
    Kort geleden heeft u zich aangemeld voor {{ fund_name }}.
    <br/>
    {{ sposor_name }} heeft uw aanmelding geaccepteerd.
    <br/>
    <br/>
    Dit betekent dat u vanaf nu uw aanbiedingen kan leveren aan klanten die recht hebben op {{ fund_name }}
    <br/>
    <br/>
    Met vriendelijke groet,
    <br/>
    <br/>
    {{ sposor_name }}
{% endblock %}
