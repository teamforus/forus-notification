
{% extends "templated_email/base.tpl" %}
{% block subject %}Totaal aantal gebruikers {{ sponsor_name }} - {{fund_name}}{% endblock %}
{% block title %}Totaal aantaal gebruikers {{ sponsor_name }} - {{ platform }}{% endblock %}
{% block html %}
    Sponsor: {{ sponsor_name }} <br />
    <br />
    Fonds: {{ fund_name }} <br />
    <br />
    Sponsors accounts: {{ sponsor_amount }}<br />
    Aanbieders accounts: {{ provider_amount }}<br />
    Aanvragers accounts: {{ requester_amount }}<br />
    <hr>
    Totaal aantal gebruikers: {{ total_amount }}<br />
{% endblock %}
