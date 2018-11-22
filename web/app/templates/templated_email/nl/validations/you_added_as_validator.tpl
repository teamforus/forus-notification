
{% extends "templated_email/base.tpl" %}
{% block subject %}{{sponsore_name}}  heeft u toegevoegd als validator{% endblock %}
{% block html %}
    Beste validator,
    <br/>
    {{ sponsore_name }} heeft u toegevoegd als validator.
    <br/>
    Vanaf nu kunt u aanvragers toevoegen, dit kunt u doen door naar het dashbaord te gaan een een .CSV bestand te uploaden.
    <br/>
{% endblock %}
