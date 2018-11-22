
{% extends "templated_email/base.tpl" %}
{% block subject %}Er staat een nieuw verzoek voor u klaar.{% endblock %}
{% block html %}
    Beste validator,
    <br/>
    Er staat een verzoek voor u klaar om eigenschappen te valideren.
    <br/>
    <br/>
    Ga naar het validator dashboard <a href="{{ validator_dashboard_link }}" target="_blank" style="color: #315efd; text-decoration: underline;">{{ validator_dashboard_link }}</a> om dit verzoek te behandelen.
{% endblock %}
