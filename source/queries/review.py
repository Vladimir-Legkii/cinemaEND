import datetime

from source.db import db_provider


def add_review(mark, id_film, login, comment, user_id):
    return db_provider.query(
        query=f"""
            INSERT INTO review (mark, date_public, id_film, login, comment, user_id)
            VALUES ({mark}, '{datetime.datetime.now()}', {id_film}, '{login}', '{comment}', {user_id});
        """,
        need_result=False,
    )


def delete_review(id_film, user_id):
    return db_provider.query(
        query=f"""
            DELETE
            FROM review
            WHERE id_film = {id_film} AND user_id = {user_id};
        """,
        need_result=False,
    )
