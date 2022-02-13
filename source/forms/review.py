from flask_wtf import FlaskForm
from wtforms import (
    IntegerField,
    TextAreaField,
    SubmitField,
)
from wtforms.validators import DataRequired


class ReviewForm(FlaskForm):

    mark = IntegerField('Mark', validators=[DataRequired()])
    comment = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Review it')


class DeleteReviewForm(FlaskForm):

    mark = IntegerField('Mark', validators=[DataRequired()])
    submit = SubmitField('Delete it')
