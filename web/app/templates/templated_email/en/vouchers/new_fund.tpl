
{% extends "templated_email/base.tpl" %}
{% block subject %}A new fund is added{% endblock %}
{% block html %}
  Dear {{username}},

    A new fund is added. Your organisation meets the requirements to apply for this fund.
    Please log in to the provider dashboard to apply for this fund.
     Thanks, you rock!
{% endblock %}