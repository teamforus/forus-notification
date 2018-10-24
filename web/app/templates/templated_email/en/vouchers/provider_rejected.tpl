
{% extends "templated_email/base.tpl" %}
{% block subject %}Your application for a fund.{% endblock %}
{% block html %}
   Dear {{ provider_name }}, <br/>

You applied to join for {{ fund_name }} a while ago. {{ sponsor_name }} of this fund has rejected your application. <br/>

Contact {{ sponsor_name }} for the reason of rejection.
{% endblock %}