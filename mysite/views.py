#import os
import page_not_found_message as pnfm
from mysite import app
from flask import render_template


# -------  primary page handlers -------
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/projects')
def work():
    return render_template('work.html')


@app.route('/about_site')
def about_site():
    return render_template('about_site.html')


# ---------- error handlers -----------
@app.errorhandler(404)
def page_not_found(e):
    message = pnfm.get_404_message()
    return render_template('404.html', error_message=message), 404
