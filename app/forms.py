from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField
from wtforms.validators import Email, DataRequired, EqualTo, ValidationError
from app import app
import random
from jinja2.utils import markupsafe

class LoginForm(FlaskForm):
    email=StringField('Email Address', validators=[DataRequired(), Email()])
    password=PasswordField('Password', validators=[DataRequired()])
    submit=SubmitField('Login')

class RegisterForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    email = StringField("Email Address", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password', message="Passwords must Match")])
    submit = SubmitField('Register')

    #has to be named like validate_COLUMNNAME
    def validate_email(form, field):
        print(field.data)
        print(app.config.get("REGISTERED_USERS"))
        if field.data.lower() in app.config.get("REGISTERED_USERS"):
            raise ValidationError("Email is Already in Use")


class EditProfileForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    email = StringField("Email Address", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password', message="Passwords must Match")])
    submit = SubmitField('Update')

    r1 = random.randint(1, 1000)
    r2 = random.randint(1001, 2000)
    r3 = random.randint(2001, 3000)
    r4 = random.randint(3001, 4000)

    r1_img = markupsafe.Markup(f'<img src="https://avatars.dicebear.com/api/adventurer/{r1}.svg" height="75px">')
    r2_img = markupsafe.Markup(f'<img src="https://avatars.dicebear.com/api/adventurer/{r2}.svg" height="75px">')
    r3_img = markupsafe.Markup(f'<img src="https://avatars.dicebear.com/api/adventurer/{r3}.svg" height="75px">')
    r4_img = markupsafe.Markup(f'<img src="https://avatars.dicebear.com/api/adventurer/{r4}.svg" height="75px">')


    icon = RadioField("Avatar", validators=[DataRequired()], choices = [(9000,"Don't Change"),(r1,r1_img),(r2,r2_img),(r3,r3_img),(r4,r4_img)])
