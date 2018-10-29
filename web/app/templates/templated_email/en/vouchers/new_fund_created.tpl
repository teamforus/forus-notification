
{% extends "templated_email/base.tpl" %}
{% block subject %}A new fund is added{% endblock %}
{% block html %}
 Dear {{requester_name}},

Dear citizen,

    A new fund has been created. You are eligible to participate in{{ fund_name }}.
    Go to <a href="{{ webshop_link }}">{{webshop_link}}</a>, log in to the webshop to sign up for {{ fund_name }}.
{% endblock %}