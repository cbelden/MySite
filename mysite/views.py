import os
from mysite import app
import jinja2


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)


@app.route('/')
def index():
    t = jinja_env.get_template('index.html')
    params = {}
    return t.render(**params)
