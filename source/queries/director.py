from source.db import db_provider


def get_director_films(id_director):
    return db_provider.query(
        query=f'''
            SELECT film.id_film, film.name_film, director.name_director, director.date_of_birth, 
                COALESCE(CAST(director.date_of_death AS CHAR(15)), '')
            FROM director
            LEFT JOIN film_director ON director.id_director = film_director.id_director
            LEFT JOIN film ON film_director.id_film = film.id_film
            WHERE director.id_director = '{id_director}';
        '''
    )


def get_director_nominations(id_director):
    return db_provider.query(
        query=f"""
            SELECT director.id_director, nomination.name_nomination, reward.name_reward
            FROM director
            JOIN presentation ON director.id_director = presentation.id_director
            JOIN nomination ON presentation.id_nomination = nomination.id_nomination
            JOIN reward ON nomination.id_reward = reward.id_reward
            WHERE director.id_director = '{id_director}';
        """
    )
