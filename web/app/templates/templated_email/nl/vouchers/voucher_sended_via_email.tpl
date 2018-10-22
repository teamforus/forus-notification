
{% extends "templated_email/base.tpl" %}
{% block subject %}Je voucher{% endblock %}
{% block html %}
Beste inwoner
<br/>
Je hebt verzocht je {{ name }} per e-mail te ontvangen.
Onderstaande QR-Code kun je gebruiken om bij een winkelier of vereniging te laten zien.
De {{ service_type }} kan deze code scannen om jouw product of dienst te leveren.

{% endblock %}