

{% extends "templated_email/base.tpl" %}
{% block subject %} {{product_name}} is toegevoegd aan de webshop{% endblock %}
{% block html %}
 Er is een nieuw product of dienst toegevoegd aan de webshop door {{provider_name}}.
Bekijk de webshop om te controleren of {{product_name}} voldoet aan de voorwaarden om vanuit het fonds aangeschaft te worden.
{% endblock %}