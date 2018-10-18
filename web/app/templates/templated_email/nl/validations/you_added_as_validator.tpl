
{% extends "templated_email/base.tpl" %}
{% block subject %}{{sponsore_name}}  heeft je toegevoegd als validator{% endblock %}
{% block html %}
  Geachte {{validator_name}},

    {{sponsore_name}} heeft je toegevoegd als validator.
Dit betekent dat je vanaf nu persoonlijke eigenschappen kan valideren.
Indien je vooraf ingestelde eigenschappen wil toevoegen kan je gebruik maken van de .CSV uploader.

{% endblock %}