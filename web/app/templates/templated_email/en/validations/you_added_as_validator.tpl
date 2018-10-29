{% extends "templated_email/base.tpl" %}

{% block subject %}{{sponsore_name}} has assigned you as a validator{% endblock %}
{% block html %}
 Beste validator, <br/>

{{ sponsore_name }} heeft je toegevoegd als validator. <br/>
Dit betekent dat je vanaf nu persoonlijke eigenschappen kan valideren.
Indien je vooraf ingestelde eigenschappen wil toevoegen kan je gebruik maken van de .CSV uploader.
{% endblock %}