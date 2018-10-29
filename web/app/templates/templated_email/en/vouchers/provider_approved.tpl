
{% extends "templated_email/base.tpl" %}
{% block subject %}Your application for {{fund_name}}{% endblock %}
{% block html %}
  Your application is accepted!

  Dear {{provider_name}},

  On {{date_start}}  you’ve signed up for {{fund_name}}. {{sponsor_name}} has accepted your application.

  From now on you can sell your products / services to customers who are eligible for {{fund_name}}
{% endblock %}