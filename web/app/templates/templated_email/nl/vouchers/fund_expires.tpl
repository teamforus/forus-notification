
{% extends "templated_email/base.tpl" %}
{% block subject %} {{fund_name}} verloopt binnenkort {% endblock %}
{% block title %} {{fund_name}} verloopt binnenkort {% endblock %}
{% block html %}
    Beste gebruik van {{fund_name}},
    <br/>
    <br/>
    Op {{start_date_fund}} heeft u van {{sponsor_name}} een {{fund_name}}-voucher ontvangen.
    Uw {{fund_name}}-voucher is geldig tot en met {{end_date_fund}}. Vanaf {{end_date_fund}} is het budget niet meer geldig.
    <br/>
    U kunt uw huidige budget en transacties inzien via: {{_shop_implementation_url}}.
    Log vervolgenns in met uw e-mailadres.
    Lukt het niet om in te loggen? Neem dan contact op met:
    <br/>
    {{phonenumber_sponsor}}
    {{emailaddress_sponsor}}
    <br/>
    We hopen u hiermee voldoende te hebben geinformeerd.
    <br/>
    Met vriendelijke groet,
    {{sponsor_name}}

{% endblock %}