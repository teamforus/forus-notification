
{% extends "templated_email/base.tpl" %}
{% block subject %} Er is een nieuw fonds toegevoegd{% endblock %}
{% block html %}
 Geachte {{requester_name}},

    Er is een nieuw fonds aangemaakt. Je voldoet aan de voorwaarden om mee te doen aan {{fund_name}}. Go naar {{link}}, log in op de webshop om je aan te melden voor dit fonds.
{% endblock %}