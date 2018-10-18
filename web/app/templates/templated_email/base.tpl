{{ TAG_START_SUBJECT }}{% autoescape off %}{% block subject %}{% endblock %}{% endautoescape %}{{ TAG_END_SUBJECT }}
{{ TAG_START_HTML }}
    <html>
        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
            <style>
                body {
                background-color: #f7f9fc;
                margin: 0;
                padding: 0;
                }
            </style>
        </head>
        <body>

            <div class="email-wrapper" style="padding: 120px 0; background-color: #f7f9fc; position: relative; background-image: url(&#39;/assets/img/projects/forus-platform/splash.png&#39;); background-repeat: no-repeat; background-position: 100% 0;">
                <div class="email-inner" style="position: relative; z-index: 1; border-radius: 10px; background-color: #fff; width: 760px; margin: auto; border: 1px solid #efefef; box-shadow: -5px 5px 15px rgba(0,0,0,.1);">
                    <div class="email-head" style="position: relative; border-bottom: 2px solid #dfe4ec; padding: 35px 0 35px;">
                        <img src="https://dt7xx7yzapqo1.cloudfront.net/static/forus-logo-color.png" style="max-height: 55px; display: block; margin: 0 auto;">
                    </div>
                    <div class="email-body" style="padding: 35px 70px 15px; border-bottom: 3px solid #dfe4ec; position: relative; text-align: center;">
                         <div class="paragraph" style="margin: 0 0 40px; font: 400 16px/24px Arial, sans-serif; color: #2b333b;">
                            {% block html %}{% endblock %}
                         </div>
                    </div>
                </div>
            </div>
            <div id="apiary-browser-extension"></div>
        </body>
    </html>
{{ TAG_END_HTML }}