

{% extends "templated_email/base.tpl" %}
{% block subject %} Er is een nieuw product of dienst toegevoegd aan de webshop.{% endblock %}
{% block html %}
Beste {{ sponsor_name }}, <br/>

Er is een nieuw product of dienst toegevoegd aan de webshop door. <br/>
Bekijk de webshop om te controleren of het voldoet aan de voorwaarden om vanuit {{ fund_name }} aangeschaft te worden.
{% endblock %}