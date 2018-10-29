
{% extends "templated_email/base.tpl" %}
{% block subject %}{{sponsore_name}}  heeft je toegevoegd als validator{% endblock %}
{% block html %}
Dear validator, <br/>

{{ sponsore_name }} has assigned you as a validator.
From now on you can validate personal records. If you want to add a batch with pre validated records, you can use the CSV uploader.

{% endblock %}