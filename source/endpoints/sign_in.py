from flask import (
    render_template,
    make_response,
    Blueprint,
    request,
    redirect,
    url_for,
)
from flask_login import login_user

from source.forms import SignInForm
from source.queries import get_user
from source.user import User


sign_in = Blueprint('sign_in', __name__)


@sign_in.route('/sign_in', methods=['GET', 'POST'])
def sign_in_page():
    """"""
    form = SignInForm()
    if request.method == 'POST':
        user = get_user(
            login=form.login.data,
            password=form.password.data,
        )
        if user:
            user = User(
                id=user[0].get('user_id'),
                login=user[0].get('login'),
            )
            login_user(user=user)
            return redirect(url_for('main.main_page'))
    return make_response(
        render_template(
            'sign_in.html',
            form=form,
        ),
        200,
        {
            'Content-Type': 'text/html',
        },
    )
