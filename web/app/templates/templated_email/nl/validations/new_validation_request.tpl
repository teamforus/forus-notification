
{% extends "templated_email/base.tpl" %}
{% block subject %}Er staat een nieuw verzoek voor je klaar.{% endblock %}
{% block html %}
  Geachte {{validator_name}},

 Er staat een verzoek voor je klaar om eigenschappen te valideren. Ga naar het validator dashboard om dit verzoek te behandelen.
{% endblock %}