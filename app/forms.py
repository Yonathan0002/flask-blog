from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Email
from app.models import User
class LoginForm(FlaskForm) :
    username = StringField('Utilisateur', validators=[DataRequired()])
    password = PasswordField('Mot de passe', validators=[DataRequired()])
    remember_me = BooleanField('Se souvenir de moi')
    submit = SubmitField('Enregistrer')

class RegistrationForm(FlaskForm):
    username = StringField(label='Utilisateur', validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Mot de passe', validators=[DataRequired()])
    password2 = PasswordField(label='Répéter le mot de passe', \
        validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Enregistrer")

    def validate_username(self: object, username: StringField) -> None:
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Choisissez un autre nom.")
            
    def validate_email(self: object,email: StringField) -> None:
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("Choisissez une autre adresse Email.")