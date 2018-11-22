
{% extends "templated_email/base.tpl" %}
{% block subject %} Er is een bedrag van je voucher afgeschreven.{% endblock %}
{% block title %}Er is een bedrag van je voucher afgeschreven.{% endblock %}
{% block html %}
    Beste inwoner,
    <br/>
    Er is zojuist een aankoop gedaan met je voucher. Hierdoor is er een bedrag afgeschreven.
Het huidige bedrag van je {{fund_name}} voucher is {{current_budget}}
{% endblock %}
