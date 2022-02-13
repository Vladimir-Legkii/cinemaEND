from flask import (
    render_template,
    make_response,
    Blueprint,
    request,
    redirect,
    url_for,
)
from flask_login import login_user

from source.forms import SignUpForm
from source.queries import (
    add_user,
    get_user,
)
from source.user import User


sign_up = Blueprint('sign_up', __name__)


@sign_up.route('/sign_up', methods=['GET', 'POST'])
def sign_up_page():
    """"""
    form = SignUpForm()

    if request.method == 'POST' and form.validate():
        login = form.login.data
        password = form.password.data
        password2 = form.password2.data

        if password == password2:
            add_user(
                login=login,
                password=password,
            )

            user = get_user(
                login=login,
                password=password,
            )

            user = User(
                id=user[0].get('user_id'),
                login=login,
            )
            login_user(user=user)
            return redirect(url_for('main.main_page'))
    return make_response(
        render_template(
            'sign_up.html',
            form=form,
        ),
        200,
        {
            'Content-Type': 'text/html',
        },
    )
