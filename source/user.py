from flask_login import UserMixin


class User(UserMixin):

    def __init__(self, id, login):
        self.id = id
        self.login = login
