
{% extends "templated_email/base.tpl" %}
{% block subject %}Uw aanbod '{{product_name}}' is verkocht!{% endblock %}
{% block title %}Uw aanbod '{{product_name}}' is verkocht!{% endblock %}
{% block html %}
    Beste gebruiker,<br/>
    <br/>
    <br/>
    Zojuist heeft iemand uw aanbieding '{{product_name}}' in de webshop gekocht. De klant kan daarom elk moment deze aanbieding komen ophalen of afnemen.<br/>
    <br/>
    De uiterlijke datum dat de klant langs kan komen is {{expiration_date}}<br/>
    <br/>
    Hopelijk hebben we u hiermee voldoende geïnformeerd.<br/>
{% endblock %}
