from flask import (
    render_template,
    make_response,
    Blueprint,
    redirect,
    url_for,
)

from source.queries import (
    get_actor_nominations,
    get_actors_films,
)


actor = Blueprint('actor', __name__)


@actor.route('/actor/<id_actor>')
def actor_page(id_actor):
    """"""
    actor = {
        'films': [],
        'nominations': [],
    }

    data_set = get_actors_films(id_actors=f"'{id_actor}'")
    if not data_set:
        return redirect(url_for('main.main_page'))

    for data in data_set:
        actor['name_actor'] = data.get('name_actor')
        actor['life_dates'] = f'{data.get("date of birth")} - {data.get("date of death", "")}'
        actor['films'].append(
            {
                'id_film': data.get('id_film'),
                'name_film': data.get('name_film'),
            },
        )

    nominations = get_actor_nominations(id_actors=f"'{id_actor}'")
    for nomination in nominations:
        actor['nominations'].append(
            f'{nomination.get("name_nomination")} - {nomination.get("name_reward")}'
        )

    return make_response(
        render_template(
            'actor.html',
            actor=actor,
        ),
        200,
        {
            'Content-Type': 'text/html',
        },
    )
