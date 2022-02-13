from source.db import db_provider


def get_user(login, password):
    return db_provider.query(
        query=f"""
            SELECT user_id, login
            FROM public.user
            WHERE login = '{login}' AND password = '{password}';
        """
    )


def get_user_by_id(id):
    return db_provider.query(
        query=f"""
            SELECT user_id, login
            FROM public.user
            WHERE user_id = '{id}';
        """
    )


def add_user(login, password):
    return db_provider.query(
        query=f"""
            INSERT INTO public.user (login, password)
            VALUES ('{login}', '{password}');
        """,
        need_result=False,
    )
