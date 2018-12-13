{% extends "templated_email/base.tpl" %}
{% block subject %}Uitverkocht: aanbod '{{product_name}}'{% endblock %}
{% block title %}Uitverkocht: aanbod '{{product_name}}' {% endblock %}
{% block button_text %}Dashboard openen{% endblock %}
{% block button_link %}{{ sponsor_dashboard_url }}{% endblock %}
{% block html %}
Beste gebruiker,<br />
<br />
Uw totale aanbod in de webshop voor '{{ product_name }}' is uitverkocht.<br />
U kunt nu het aanbod aanvullen of verwijderen. Als u het aanbod verwijderd kunt u daarna een nieuw aanbod plaatsen.<br />
<br />
Dit kunt u doen door in te loggen op het dashboard. Klik <a href="{{ sponsor_dashboard_url }}" target="_blank" style="color: #315efd; text-decoration: underline;">hier</a> of op de knop hieronder om naar het dashboard te gaan. <br/>
{% endblock %}
