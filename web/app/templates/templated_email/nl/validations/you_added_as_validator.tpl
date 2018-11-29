
{% extends "templated_email/base.tpl" %}
{% block subject %}{{sponsore_name}}  heeft u toegevoegd als validator{% endblock %}
{% block html %}
    Beste validator,
    <br/>
    <br/>
    {{ sponsore_name }} heeft u toegevoegd als validator.
    <br/>
    Vanaf nu kunt u aanvragers toevoegen, dit kunt u doen door naar het dashboard te gaan een een .CSV bestand te uploaden.
    <br/>
{% endblock %}
