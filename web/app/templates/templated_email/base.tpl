{{ TAG_START_SUBJECT }}{% autoescape off %}{% block subject %}{% endblock %}{% endautoescape %}{{ TAG_END_SUBJECT }}
{{ TAG_START_HTML }}

    <html>
        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        </head>
        <body style="width: 100% !important; -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; background: #f6f5f5; margin: 0; padding: 0;" bgcolor="#f6f5f5">
            <center>
                <table id="wrapperTable" cellpadding="0" cellspacing="0" border="0" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-size: 0; width: 100% !important; max-width: 600px !important; line-height: 100% !important; background: #fff; margin: 0 auto; padding: 0;" bgcolor="#fff">
                    <tr>
                        <td valign="top" align="center" style="border-collapse: collapse;">
                            <div id="wrapper" style="font-family: Helvetica, Arial, ArialMT, sans-serif; width: 100%; max-width: 600px; overflow: hidden; color: #2e3238; font-size: 0; background: #f6f5f5; margin: 0 auto;">
                                <!--<table cellpadding="0" cellspacing="0" border="0" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-size: 0; width: 100% !important; text-align: center; margin: 0px auto;">
                                    <tr>
                                        <td style="border-collapse: collapse; padding-top: 30px; padding-bottom: 26px;">
                                            <img src="https://media.forus.io/static/logo_black_200x38.png" style="width: 100px; display: block; margin: 0 auto;">
                                        </td>
                                    </tr>
                                </table>-->
                                <table cellpadding="0" cellspacing="0" border="0" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-size: 0; width: 100% !important; text-align: center; background: #fff; margin: 0px auto;" bgcolor="#fff">
                                    <tr>
                                        <td style="border-collapse: collapse; padding: 24px 24px 32px;">
                                                <h1 style="margin: 0 auto; color: #2e3238; font-size: 36px; line-height: 1.1; font-weight: bold;"> {% block title %}{% endblock %}</h1>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="border-collapse: collapse; padding-bottom: 25px;">
                                            <img src="{% block header_image %}" style="width: 297px; display: block; margin: 0 auto;"> {% endblock %}
                                        </td>
                                    </tr>
                                    <tr>
                                        <td align="center" style="border-collapse: collapse; padding-left: 24px; padding-right: 24px;">
                                            <p style="margin: 0; color: #2e3238; font-family: Helvetica, Arial, sans-serif; font-size: 16px; line-height: 24px;">
                                                {% block html %}{% endblock %}
                                            </p>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td align="center" style="border-collapse: collapse; padding-bottom: 25px;">
                                        </td>
                                    </tr>
                                    <tr>
                                        <td align="center" style="border-collapse: collapse;">
                                            <table cellpadding="0" cellspacing="0" border="0" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-size: 0; width: 166px!important; text-align: center; margin: 0px auto;">
                                                <tr>
                                                    <td align="center" style="border-collapse: collapse; background: #315efd; border-radius: 3px;">
                                                        <a href="{% block button_link %}{% endblock %}" target="_blank" style="display: block; width: 100%; text-align: center; color: #fff; font-size: 14px; font-weight: bold; letter-spacing: 2px; line-height: 46px; text-transform: uppercase; text-decoration: none;">{% block button_text %}{% endblock %}</a>
                                                    </td>
                                                </tr>
                                            </table>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td align="center" style="border-collapse: collapse; padding-bottom: 25px;">
                                        </td>
                                    </tr>
                                </table>
                                <!--<table cellpadding="0" cellspacing="0" border="0" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-size: 0; width: 100% !important; text-align: center; margin: 0px auto;">
                                    <tr>
                                        <td align="center" style="border-collapse: collapse; padding-top: 22px; padding-bottom: 37px">
                                            <p style="margin: 0; color: #2e3238; font-family: Helvetica, Arial, sans-serif; font-size: 12px; line-height: 22px;">
                                                <a href="mailto:info@forus.io" style="color: #2e3238; text-decoration: underline;">info@forus.io</a>
                                                <br />
                                                Foundation Forus, Groningen, Netherlands
                                            </p>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td align="center" style="border-collapse: collapse; padding-bottom: 10px;">
                                            <img src="https://media.forus.io/static/logo_black_200x38.png" style="width: 52px; display: block; margin: 0 auto; opacity: 0.5;">
                                        </td>
                                    </tr>

                                </table>-->
                            </div>
                        </td>
                    </tr>
                </table>
            </center>
        </body>
    </html>
{{ TAG_END_HTML }}

