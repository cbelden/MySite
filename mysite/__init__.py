from flask import Flask, url_for, session


app = Flask(__name__)
import mysite.views
