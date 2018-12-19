
{% extends "templated_email/base.tpl" %}
{% block subject %} {{fund_name}} is van start gegaan{% endblock %}
{% block title %} {{fund_name}} is van start gegaan{% endblock %}
{% block html %}
    Beste aanbieder,
    <br/>
    <br/>
    U bent onlangs goedgekeurd door {{sponsor_name}} om deel te nemen aan {{fund_name}}.
    <br/>
    Vanaf vandaag is dit fonds actief, dit betekent dat u vanaf vandaag klanten kan verwachten die gebruik willen maken van hun {{fund_name}}-voucher.
    <br/>

{% endblock %}