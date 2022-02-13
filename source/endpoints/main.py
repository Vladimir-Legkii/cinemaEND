from flask import (
    render_template,
    make_response,
    Blueprint,
)
from flask_login import current_user

from source.queries import (
    get_films,
)


main = Blueprint('main', __name__)


@main.route('/')
def main_page():
    """"""
    return make_response(
        render_template(
            'main.html',
            is_authorized=current_user.is_authenticated,
            films=get_films(),
        ),
        200,
        {
            'Content-Type': 'text/html',
        },
    )
