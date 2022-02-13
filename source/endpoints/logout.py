from flask import (
    Blueprint,
    redirect,
    url_for,
)
from flask_login import logout_user


logout = Blueprint('logout', __name__)


@logout.route('/logout')
def logout_page():
    """"""
    logout_user()
    return redirect(url_for('main.main_page'))
