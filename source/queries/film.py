from source.db import db_provider


def get_films():
    return db_provider.query(
        query='''
            SELECT film.id_film, film.name_film, film.release_date, film.age, film.url, 
                director.id_director, director.name_director 
            FROM film
            LEFT JOIN film_director ON film.id_film = film_director.id_film
            LEFT JOIN director ON film_director.id_director = director.id_director;
        '''
    )


def get_film(id_film):
    return db_provider.query(
        query=f'''
            SELECT film.id_film, film.name_film, film.release_date, film.age, film.url, 
                director.id_director, director.name_director, director.date_of_birth, 
                COALESCE(CAST(director.date_of_death AS CHAR(15)), '')
            FROM film
            LEFT JOIN film_director ON film.id_film = film_director.id_film
            LEFT JOIN director ON film_director.id_director = director.id_director
            WHERE film.id_film = '{id_film}';
        '''
    )


def get_reviews(id_film):
    return db_provider.query(
        query=f'''
            SELECT film.id_film, review.login, review.mark, review.date_public, review.comment, review.user_id
            FROM film 
            LEFT JOIN review ON film.id_film = review.id_film
            WHERE film.id_film = '{id_film}';
        '''
    )


def get_genres(id_film):
    return db_provider.query(
        query=f'''
            SELECT film.id_film, genre.name AS genre
            FROM film
            LEFT JOIN genre_film ON film.id_film = genre_film.id_film
            LEFT JOIN genre ON genre_film.id_genre = genre.id_genre
            WHERE film.id_film = '{id_film}';
        '''
    )


def get_rewards(id_film):
    return db_provider.query(
        query=f'''
            SELECT film.id_film, nomination.name_nomination, reward.name_reward
            FROM film
            LEFT JOIN presentation ON film.id_film = presentation.id_film
            LEFT JOIN nomination ON presentation.id_nomination = nomination.id_nomination
            LEFT JOIN reward ON nomination.id_reward = reward.id_reward
            WHERE film.id_film = '{id_film}';
        '''
    )


def get_actors(id_film):
    return db_provider.query(
        query=f'''
            SELECT film.id_film, actor.id_actor, actor.name_actor
            FROM film 
            LEFT JOIN role ON film.id_film = role.id_film
            LEFT JOIN actor ON role.id_actor = actor.id_actor
            WHERE film.id_film = '{id_film}';
        '''
    )
