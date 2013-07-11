import os
import page_not_found_message as pnfm
from mysite import app
from flask import render_template


@app.route('/')
def index():
    params = {}
    return render_template('sample.html', **params)

@app.errorhandler(404)
def page_not_found(e):
    message = pnfm.get_404_message()
    return render_template('404.html', error_message=message), 404

@app.route('/practice')
def practice():
    return render_template('grid_practice.html')
