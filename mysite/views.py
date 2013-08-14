import business.page_not_found_message as pnfm
import business.message as msg
from mysite import app
from flask import render_template, request


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


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        try:
            msg.send_email(request.form)
        except Exception, e:
            return render_template('message_error.html', error=e)
        return render_template('thank_you.html', name=request.form['name'].split(' ').capitalize())
    else:
        return render_template('contact.html')


# ---------- error handlers -----------
@app.errorhandler(404)
def page_not_found(e):
    message = pnfm.get_404_message()
    return render_template('404.html', error_message=message), 404
