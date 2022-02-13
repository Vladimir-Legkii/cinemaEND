from source.db import db_provider


def get_actors_films(id_actors):
    return db_provider.query(
        query=f"""
            SELECT actor.id_actor, actor.name_actor, "date of birth", 
                COALESCE(CAST("date of death" AS CHAR(15)), '') as "date of death", 
                film.id_film, film.name_film
            FROM actor
            LEFT JOIN role ON actor.id_actor = role.id_actor
            LEFT JOIN film ON film.id_film = role.id_film
            WHERE actor.id_actor IN ({id_actors});
        """
    )


def get_actor_nominations(id_actors):
    return db_provider.query(
        query=f"""
            SELECT actor.id_actor, nomination.name_nomination, reward.name_reward
            FROM actor
            JOIN presentation ON actor.id_actor = presentation.id_actor
            JOIN nomination ON presentation.id_nomination = nomination.id_nomination
            JOIN reward ON nomination.id_reward = reward.id_reward
            WHERE actor.id_actor IN ({id_actors});
        """
    )
