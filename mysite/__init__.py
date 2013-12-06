from flask import Flask
from flask.ext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# configure mail settings
app.config.update(
    MAIL_SERVER='smtp.live.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USE_SSL=False,
    MAIL_USERNAME=os.environ['EMAIL_ADDRESS'],
    MAIL_PASSWORD=os.environ['EMAIL_PASSWORD'])

# configure db settings
app.config.update(
    SQLALCHEMY_DATABASE_URI=os.environ['DATABASE_URL'])

db = SQLAlchemy(app)
mail = Mail(app)

import mysite.views