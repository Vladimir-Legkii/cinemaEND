from collections import defaultdict

from flask import (
    render_template,
    make_response,
    Blueprint,
    request,
    redirect,
    url_for,
)
from flask_login import current_user

from source.forms import (
    ReviewForm,
    DeleteReviewForm,
)
from source.queries import (
    get_film,
    get_reviews,
    get_genres,
    get_rewards,
    get_actors,
    add_review,
    delete_review,
)


film = Blueprint('film', __name__)


@film.route('/film/<id_film>', methods=['GET', 'POST'])
def film_page(id_film):
    """"""
    error_msg = ''
    form = ReviewForm()
    delete_form = DeleteReviewForm()
    if request.method == 'POST':
        if form.validate():
            try:
                if 0 <= form.mark.data <= 10:
                    add_review(
                        mark=form.mark.data,
                        id_film=id_film,
                        login=current_user.login,
                        comment=form.comment.data,
                        user_id=current_user.id,
                    )
            except Exception:
                error_msg = 'You already exist review'
        elif delete_form.submit():
            try:
                delete_review(
                    id_film=id_film,
                    user_id=current_user.id,
                )
            except Exception:
                error_msg = 'Something went wrong with deleting'

    data = get_reviews(id_film)
    reviews = defaultdict(list)
    for review in data:
        reviews[review.get('id_film')].append(list(review.values()))

    data = get_genres(id_film)
    genres = defaultdict(list)
    for genre in data:
        genres[genre.get('id_film')].append(genre.get('genre'))

    data = get_rewards(id_film)
    nominations = defaultdict(list)
    rewards = defaultdict(list)
    for nomination_reward in data:
        id_film = nomination_reward.get('id_film')

        if name_nomination := nomination_reward.get('name_nomination'):
            nominations[id_film].append(name_nomination)

        if name_reward := nomination_reward.get('name_reward'):
            rewards[id_film].append(name_reward)

    data = get_actors(id_film)
    actors = defaultdict(list)
    for actor in data:
        actors[actor.get('id_film')].append(actor)

    film = get_film(id_film)
    if not film:
        return redirect(url_for('main.main_page'))

    film = film[0]
    id_film = film.get('id_film')

    film['reviews'] = reviews.get(id_film, [])
    film['genres'] = genres.get(id_film, [])
    film['nominations'] = nominations.get(id_film, ['N/A'])
    film['rewards'] = rewards.get(id_film, ['N/A'])
    film['actors'] = actors.get(id_film, [])

    return make_response(
        render_template(
            'film.html',
            current_user_id=current_user.id,
            is_authorized=current_user.is_authenticated,
            film=film,
            form=form,
            delete_form=delete_form,
            error_msg=error_msg,
        ),
        200,
        {
            'Content-Type': 'text/html',
        },
    )