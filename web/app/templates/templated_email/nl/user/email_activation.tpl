
{% extends "templated_email/base.tpl" %}
{% block subject %}E-mail activering{% endblock %}
{% block button_text %}Verifieer{% endblock %}
{% block button_link %}{{ link }}{% endblock %}
{% block title %}E-mail activering{% endblock %}
{% block header_image %} https://media.forus.io/static/iphone_shield_594x594.png {% endblock %}
{% block html %}
    U krijgt deze e-mail omdat u op {{ platform }} uw email adres hebt ingevuld. Met deze e-mail willen we verifieren of u toegang heeft tot dit e-mailadres.
    <br/>
    <br/>
    Als u op deze <a style="color: #315efd; text-decoration: underline;" href="{{ link }}" target="blank">link</a> klikt of op de onderstaande knop wordt uw e-mailadres geverifieerd.
    <br/>
{% endblock %}