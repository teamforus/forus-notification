
{% extends "templated_email/base.tpl" %}
{% block subject %}Er is een nieuw fonds toegevoegd{% endblock %}
{% block html %}
    Beste inwoner,
    <br/>
    Er is een nieuw fonds aangemaakt. Je voldoet aan de voorwaarden om mee te doen aan {{ fund_name }}.
    <br/>
    <br/>
    Go naar <a href="{{ webshop_link }}" target="_blank" style="color: #315efd; text-decoration: underline;">{{webshop_link}}</a>, log in op de webshop om je aan te melden voor {{ fund_name }}.

{% endblock %}