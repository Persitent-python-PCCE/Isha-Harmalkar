from flask_wtf import FlaskForm

from wtforms import(
    StringField,
    PasswordField,
    SubmitField
)


from wtforms.validators import (
    DataRequired,
    Email,
    Length,
    EqualTo
)

class RegisterForm(FlaskForm):

    name = StringField(
        "Name",
        validators=[
            DataRequired(),
            Length(min=2, max=100)
        ]
    )

    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email()
        ]
    )


    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=6)
        ]
    )

    confirmPassword = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(),
            EqualTo("password",
            message="Passwords must match"
            )
        ]
    )

    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired()
        ]

    )


    submit = SubmitField("Login")
    