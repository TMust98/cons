from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, EqualTo, Length
from app.models import Users


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня!')
    submit = SubmitField('Войти')


class RegistrationForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password2 = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')])
    dment = StringField('Отдел из списка доступных', validators=[DataRequired()])#SelectField
    dment_RU = StringField('Отдел на русском', validators=[DataRequired()])
    fio = StringField('Фамилия И.О.', validators=[DataRequired()])
    dm_Head = BooleanField('Начальник отдела?')
    submit = SubmitField('Регистрация')

    def validate_username(self, username):
        user = Users.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Пожалуйста введите другое имя пользователя!')


class ChangeDmentForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password2 = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')])
    Dment = StringField('Отдел', validators=[DataRequired()])#SelectField
    submit = SubmitField('Регистрация')

    def validate_username(self, username):
        user = Users.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Пожалуйста введите другое имя пользователя!')


class AddContract(FlaskForm):
    KTRU = StringField("ИКЗ", validators=[DataRequired()])
    Name = StringField("Название", validators=[DataRequired()])
    StageTZ = TextAreaField("Этап ТЗ", validators=[DataRequired()])
    PlanSrokRazm = StringField("Плановый срок размещения", render_kw={"placeholder": "Март 2022"})
    submit = SubmitField('Внести')


class ShowConForm(FlaskForm):
    Dment = StringField("Отдел", render_kw={"readonly": True})
    Who = StringField("Ответственный", render_kw={"readonly": True})
    KTRU = StringField("ИКЗ", render_kw={"readonly": True})
    Name = StringField("Название", render_kw={"readonly": True})
    StageTZ = TextAreaField("Этап ТЗ", render_kw={"readonly": True})
    PlanSrokRazm = StringField("Плановый срок размещения", render_kw={"placeholder": "Март 2022", "readonly": True})
    DateSendToKom = StringField("Дата отправки в комитет проекта контракта", render_kw={"placeholder": "ДД.ММ.ГГГГ", "readonly": True})
    DateOfContract = StringField("Дата заключения контракта", render_kw={"placeholder": "ДД.ММ.ГГГГ", "readonly": True})
    NGosContract = StringField("Номер ГК", render_kw={"readonly": True})
    Organization = StringField("Организация", render_kw={"readonly": True})
    SrokPostavkiPoGK = StringField("Срок поставки по ГК", render_kw={"placeholder": "ДД.ММ.ГГГГ", "readonly": True})
    Pretensii = StringField("Претензии", render_kw={"readonly": True})
    RabWDocs = StringField("Работа с документами", render_kw={"readonly": True})
    DateGiveToKom = StringField("Дата сдачи в комитет", render_kw={"placeholder": "ДД.ММ.ГГГГ", "readonly": True})
    submit = SubmitField('Внести изменения')


class EditConForm(FlaskForm):
    KTRU = StringField("ИКЗ", validators=[DataRequired()])
    Name = StringField("Название", validators=[DataRequired()])
    StageTZ = TextAreaField("Этап ТЗ", validators=[DataRequired()])
    PlanSrokRazm = StringField("Плановый срок размещения", render_kw={"placeholder": "Март 2022"})
    DateSendToKom = StringField("Дата отправки в комитет проекта контракта", render_kw={"placeholder": "ДД.ММ.ГГГГ"})
    DateOfContract = StringField("Дата заключения контракта", render_kw={"placeholder": "ДД.ММ.ГГГГ"})
    NGosContract = StringField("Номер ГК")
    Organization = StringField("Организация")
    SrokPostavkiPoGK = StringField("Срок поставки по ГК", render_kw={"placeholder": "ДД.ММ.ГГГГ"})
    Pretensii = StringField("Претензии")
    RabWDocs = StringField("Работа с документами")
    DateGiveToKom = StringField("Дата сдачи в комитет", render_kw={"placeholder": "ДД.ММ.ГГГГ"})
    submit = SubmitField('Внести изменения')