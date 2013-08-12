from flask import Flask
from flask.ext.mail import Mail
import os

app = Flask(__name__)
mail = Mail(app)

# configure mail settings
app.config.update(
    MAIL_SERVER='smtp.live.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USE_SSL=False,
    MAIL_USERNAME=os.environ['EMAIL_ADDRESS'],
    MAIL_PASSWORD=os.environ['EMAIL_PASSWORD'])


mail = Mail(app)

import mysite.views
