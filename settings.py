from flask import Flask

from flask_login import LoginManager


application = Flask(
    import_name=__name__,
    static_folder='static',
    template_folder='templates',
)

application.config['SECRET_KEY'] = 'secret_key'

login = LoginManager(application)
