
{% extends "templated_email/base.tpl" %}
{% block subject %}Uw aanmelding voor een fonds.{% endblock %}
{% block title %} {{ provider_name }} wilt zich aanmelden voor {{ fund_name }}{% endblock %}
{% block html %}
    Beste {{ provider_name }},
    <br/>
    <br/>
    Onlangs heeft u zich aangemeld voor {{ fund_name }}.
    <br/>
    {{ sponsor_name }} heeft uw aanmelding beoordeeld en heeft besloten dat u voor {{ fund_name }} bent afgewezen.
    <br/>
    <br/>
    Mocht u hierover meer willen weten, dan kunt u contact opnemen met {{ sponsor_name }}.
    <br />
    Telefoonnummer: {{ sponsor_phone }}
    <br />
    We hopen u hiermee voldoende te hebben geïnformeerd.
    <br/>
    <br/>
    Met vriendelijke groet,
    <br/>
    <br/>
    Team {{ fund_name }}
{% endblock %}
