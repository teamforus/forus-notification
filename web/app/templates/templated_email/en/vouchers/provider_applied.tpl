
{% extends "templated_email/base.tpl" %}
{% block subject %}{{provider_name}} wants to register for {{fund_name}}{% endblock %}
{% block html %}

  Dear {{sponsor_name}},

  A registration has been received from {{provider_name}} to participate in {{fund_name}}.
  Check whether this provider meets your conditions to participate. Log in to the sponsor dashboard to process this registration.
{% endblock %}