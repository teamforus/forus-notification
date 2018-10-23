
{% extends "templated_email/base.tpl" %}
{% block subject %}There is a new request waiting for you.{% endblock %}
{% block html %}
  Dear {{validator_name}},

 There is a request for you to validate records.
 Go to the validator dashboard to process this request.
{% endblock %}