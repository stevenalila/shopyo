from flask_wtf import FlaskForm

# from wtforms.validators import Length
# from wtforms.fields.html5 import EmailField
from wtforms import (
    PasswordField,
    SelectField,
    StringField,
    SubmitField,
    TextAreaField,
    TextField,
)
from wtforms.validators import DataRequired

from shopyoapi.validators import verify_slug


class PageForm(FlaskForm):

    content = TextAreaField(
        "Content",
        [],
        render_kw={"class": "form-control", "rows": "20", "autocomplete": "off"},
    )
    slug = StringField(
        "Slug",
        [DataRequired(), verify_slug],
        render_kw={"class": "form-control", "autocomplete": "off"},
    )
    title = StringField(
        "Title",
        [DataRequired()],
        render_kw={"class": "form-control", "autocomplete": "off"},
    )
