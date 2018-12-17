
{% extends "templated_email/base.tpl" %}
{% block subject %}Er is een bedrag van uw voucher afgeschreven.{% endblock %}
{% block title %}Er is een bedrag van uw voucher afgeschreven.{% endblock %}
{% block html %}
    Beste gebruiker,
    <br/>
    <br/>
    Er is zojuist een aankoop gedaan met je voucher. Hierdoor is er een bedrag afgeschreven.
Het huidige bedrag van je {{fund_name}} voucher is {{current_budget}}
{% endblock %}
