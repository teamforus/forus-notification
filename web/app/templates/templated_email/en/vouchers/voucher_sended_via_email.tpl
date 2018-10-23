
{% extends "templated_email/base.tpl" %}
{% block subject %}Your voucher{% endblock %}
{% block html %}
    Dear citizen,
<br/>
You’ve requested to receive your {{ name }} by e-mail.
You can use the QR-Code below to show to a provider.
They will scan your code and deliver your product / service.
{% endblock %}