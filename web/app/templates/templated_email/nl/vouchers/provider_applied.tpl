{% extends "templated_email/base.tpl" %}
{% block subject %}{{provider_name}} heeft zich aangemeld voor {{fund_name}}{% endblock %}
{% block html %}

  <b>Beste {{sponsor_name}}</b>,<br/>
  <br />
  Er is een aanmelding binnengekomen van {{provider_name}} om deel te nemen aan een fonds dat u beheert, {{fund_name}}.<br />
  Controleer of deze leverancier voldoet aan uw voorwaarden om deel te nemen. <br />
  <br />
  <div class="paragraph" style="margin: 0 0 40px; font: 400 16px/24px Arial, sans-serif; color: #2b333b;">
     <a href="https://forus.link/sponsor/#!/" style="display: inline-block; padding: 5px 75px; font: 600 14px/40px Arial, sans-serif; color: #fff; border-radius: 3px; text-decoration: none;background-color: #305dfb;">
     AANMELDEN ALS SPONSOR
     </a>
  </div>
{% endblock %}
