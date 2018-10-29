
{% extends "templated_email/base.tpl" %}
{% block subject %}Er is een nieuw fonds toegevoegd{% endblock %}
{% block html %}
 Beste inwoner,

 Er is een nieuw fonds aangemaakt. Je voldoet aan de voorwaarden om mee te doen aan {{ fund_name }}.
     Go naar <a href="{{ webshop_link }}">{{webshop_link}}</a>, log in op de webshop om je aan te melden voor {{ fund_name }}.

{% endblock %}