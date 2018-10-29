
{% extends "templated_email/base.tpl" %}
{% block subject %}Je aanmelding voor {{fund_name}}{% endblock %}
{% block html %}
  Je aanmelding is geaccepteerd! <br/> <br/>

Beste  {{ provider_name }}, <br/>
Kort geleden heb je je aangemeld voor {{ fund_name }}.{{ sposor_name }} heeft je aanmelding geaccepteerd. <br/><br/>

Dit betekent dat je vanaf nu je producten en/of diensten kan leveren aan klanten die recht hebben op {{ fund_name }}
{% endblock %}