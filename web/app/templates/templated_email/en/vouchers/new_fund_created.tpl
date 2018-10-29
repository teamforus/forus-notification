
{% extends "templated_email/base.tpl" %}
{% block subject %}A new fund is added{% endblock %}
{% block html %}
 Dear {{requester_name}},

    A new fund has been created. You are eligible to participate in {{fund_name}}. Go to {{link}}, log in to the web-shop to sign up for this fund.
{% endblock %}