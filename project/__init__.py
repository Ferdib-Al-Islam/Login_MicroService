from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

app.config.update(dict(
    DEBUG=True,
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))

from project.api.routes import api_index
from project.site.routes import site_index
from project.admin.routes import admin_index

app.register_blueprint(site_index)
app.register_blueprint(api_index, url_prefix='/api')
app.register_blueprint(admin_index, url_prefix='/admin')
