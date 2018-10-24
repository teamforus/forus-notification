
{% extends "templated_email/base.tpl" %}
{% block subject %}Je aanmelding voor een fonds.{% endblock %}
{% block html %}
    Beste {{ provider_name }}, <br/>

Kort geleden heb je je aangemeld voor {{ fund_name }}.
{{ sponsor_name }} heeft je aanmelding afgewezen.

Wil je hiervan de reden weten? Neem dan contact op met {{ sponsor_name }}.

{% endblock %}