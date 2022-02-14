from flask import (
    render_template,
    make_response,
    Blueprint,
    redirect,
    url_for,
)

from source.queries import (
    get_director_films,
    get_director_nominations,
)


director = Blueprint('director', __name__)


@director.route('/director/<id_director>')
def director_page(id_director):
    """"""
    director = {
        'films': [],
        'nominations': ['N/A'],
    }

    data_set = get_director_films(id_director=id_director)
    if not data_set:
        return redirect(url_for('main.main_page'))

    for data in data_set:
        director['name_director'] = data.get('name_director')
        director['life_dates'] = f'{data.get("date_of_birth")} - {data.get("date_of_death", "")}'
        director['films'].append(
            {
                'id_film': data.get('id_film'),
                'name_film': data.get('name_film'),
            },
        )

    nominations = get_director_nominations(id_director=id_director)
    data_nominations = []
    for nomination in nominations:
        data_nominations.append(
            f'{nomination.get("name_nomination")} - {nomination.get("name_reward")}'
        )
    if data_nominations:
        director['nominations'] = data_nominations

    return make_response(
        render_template(
            'director.html',
            director=director,
        ),
        200,
        {
            'Content-Type': 'text/html',
        },
    )
