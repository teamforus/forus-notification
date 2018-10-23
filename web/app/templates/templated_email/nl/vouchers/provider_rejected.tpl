
{% extends "templated_email/base.tpl" %}
{% block subject %}{{ product_name }} voucher is niet meer geldig.{% endblock %}
{% block html %}
    Beste inwoner,
    <br/>
    {{ sponsor_name }} heeft {{ provider_name }}
    geweigerd om verder deel te nemen als leverancier voor {{ fund_name }}. Dit betekent dat je {{ product_name }} voucher niet langer kan gebruiken.
    Onze excuses voor het ongemak.

{% endblock %}