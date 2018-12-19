
{% extends "templated_email/base.tpl" %}
{% block subject %}Uw voucher{% endblock %}
{% block title %}Uw voucher{% endblock %}
{% block html %}
    Beste gebruiker,
    <br/>
    <br/>
    U heeft gevraagd uw {{fund_product_name}}-voucher per e-mail te ontvangen.
    <br/>
    Onderstaande QR-code laat u bij de aanbieder zien.
    <br/>
    De aanbieder scant deze code en de betaling gebeurt automatisch, daar hoeft u niks voor te doen.
    <br/>
    <br/>
    <img style="display: block; margin: 0 auto;" src="{{ qr_url }}" width="300" />
{% endblock %}
