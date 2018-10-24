
{% extends "templated_email/base.tpl" %}
{% block subject %}Er staat een nieuw verzoek voor je klaar.{% endblock %}
{% block html %}
Beste validator, <br/>

Er staat een verzoek voor je klaar om eigenschappen te valideren. Ga naar het validator dashboard <a href="{{ validator_dashboard_link }}">{{ validator_dashboard_link }}</a> om dit verzoek te behandelen.
{% endblock %}