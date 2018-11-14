
{% extends "templated_email/base.tpl" %}
{% block subject %}There is a new request waiting for you.{% endblock %}
{% block html %}
    Dear validator,
    <br/>
    There is a request for you to validate records.
    <br/>
    <br/>
    Go to the validator dashboard <a href="{{ validator_dashboard_link }}" target="_blank" style="color: #315efd; text-decoration: underline;">{{ validator_dashboard_link }}</a> to process this request.
{% endblock %}