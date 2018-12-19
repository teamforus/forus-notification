
{% extends "templated_email/base.tpl" %}
{% block subject %} {{fund_name}} will expire soon {% endblock %}
{% block title %} {{fund_name}} will expire soon {% endblock %}
{% block html %}
    Dear user of {{fund_name}},
    <br/>
    <br/>
    On {{start_date_fund}} you received from {{sponsor_name}} a {{fund_name}}-voucher.
    <br/>
    Your {{fund_name}}-voucher is valid until {{end_date_fund}}. After {{end_date_fund}} your voucher will expire.
    <br/>
    You can see your current budget on the webshop: {{shop_implementation_url}}.
    <br/>
    Login with your e-mailaddress.
    <br/>
    If you can't login, pleas contact:
    <br/>
    {{phonenumber_sponsor}}
    <br/>
    {{emailaddress_sponsor}}
    <br/>
    We hope to have sufficiently informed you
    <br/>
    Sincerely,
    {{sponsor_name}}

{% endblock %}