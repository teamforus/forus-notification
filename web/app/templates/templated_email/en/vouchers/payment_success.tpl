
{% extends "templated_email/base.tpl" %}
{% block subject %} Successful payment with your voucher!{% endblock %}
{% block title %}Successful payment with your voucher!{% endblock %}
{% block html %}
    Dear user,
    <br/>
    A purchase has just been made with your voucher.
    Currently there is {{current_budget}} on your {{fund_name}} voucher.
{% endblock %}
