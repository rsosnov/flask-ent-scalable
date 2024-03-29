from flask_wtf import FlaskForm as Form
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length


class CommentForm(Form):
    name = StringField("Name",
                       validators=[DataRequired(), Length(max=255)])
    text = TextAreaField("Comment", validators=[DataRequired()])


class PostForm(Form):
    title = StringField("Title", [DataRequired(), Length(max=255)])
    youtube_id = StringField("Youtube video id", [Length(max=255)])
    text = TextAreaField("Content", [DataRequired()])
