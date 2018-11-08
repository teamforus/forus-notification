
{% extends "templated_email/base.tpl" %}
{% block subject %}{{ product_name }} voucher is no longer valid.{% endblock %}
{% block html %}
    Dear {{ provider_name }},
    <br/>
    You applied to join for {{fund_name }} a while ago.
    <br/>
    {{ name_sponsor }} of this fund has rejected your application.
    <br/>
    <br/>
    Contact {{ sponsor_name }} for the reason of rejection.
{% endblock %}