from source.queries import get_user_by_id
from settings import (
    application,
    login,
)
from source import endpoints
from source.user import User


application.register_blueprint(endpoints.main)
application.register_blueprint(endpoints.sign_in)
application.register_blueprint(endpoints.sign_up)
application.register_blueprint(endpoints.logout)
application.register_blueprint(endpoints.film)
application.register_blueprint(endpoints.actor)
application.register_blueprint(endpoints.director)


@login.user_loader
def load_user(user_id):
    """"""
    user = get_user_by_id(
        id=user_id,
    )
    if not user:
        return None
    return User(
        id=user[0].get('user_id'),
        login=user[0].get('login'),
    )


if __name__ == '__main__':
    application.run()
