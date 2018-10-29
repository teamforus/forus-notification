
{% extends "templated_email/base.tpl" %}
{% block subject %}Your login details{% endblock %}
{% block html %}
Dear citizen,

You’ve just requested to login on to the {{ platform }}.
Click on the <a href="{{ link }}">link</a> below to continue logging in.
<br/>
<a href="{{ link }}">{{ link }}</a>
{% endblock %}