
{% extends "templated_email/base.tpl" %}
{% block subject %}Er is een nieuw fonds toegevoegd: {{fund_name}} {% endblock %}
{% block html %}
    Beste Forus,
    <br/>
    Er is een nieuw fonds aangemaakt: {{fund_name}}     <br/>
    Door: {{sponsor_name}}    <br/>
    <br/>
{% endblock %}
