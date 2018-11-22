
{% extends "templated_email/base.tpl" %}
{% block subject %}Je voucher{% endblock %}
{% block html %}
    Beste inwoner
    <br/>
    U heeft verzocht uw {{fund_product_name}} voucher per e-mail te ontvangen.
    <br/>
    Onderstaande QR-Code kunt u gebruiken om bij een winkelier of vereniging te laten zien.
    <br/>
    De winkelier / vereniging kan deze code scannen om uw product of dienst te leveren.
    <br/>
    <br/>
    <img style="display: block; margin: 0 auto;" src="{{ qr_url }}" width="300" />
{% endblock %}
