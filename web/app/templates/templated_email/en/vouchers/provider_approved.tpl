
{% extends "templated_email/base.tpl" %}
{% block subject %}Your application for {{fund_name}}{% endblock %}
{% block html %}
  Your application is accepted! <br/><br/>

Dear {{ provider_name }}, <br/>
You applied to join for {{ name_fund }} a while ago. <br/>
The {{ name_sponsor }} has accepted your application. <br/>

From now on you can sell your products / services to customers who are eligible for {{ fund_name }}
{% endblock %}