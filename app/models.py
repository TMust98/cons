from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login


class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    Dment = db.Column(db.String(15))
    Dment_RU = db.Column(db.String(15))
    FIO = db.Column(db.String(30))
    Dment_head = db.Column(db.Boolean)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class ConPTV(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Dment = db.Column(db.String(15), nullable=False)
    Dment_en = db.Column(db.String(15))
    Who = db.Column(db.String(15), nullable=False)
    KTRU = db.Column(db.String(20))
    Name = db.Column(db.String(20))
    StageTZ = db.Column(db.Text)
    PlanSrokRazm = db.Column(db.String(15))
    DateSendToKom = db.Column(db.Date)
    DateOfContract = db.Column(db.Date)
    NGosContract = db.Column(db.Integer)
    Organization = db.Column(db.String(15))
    SrokPostavkiPoGK = db.Column(db.Date)
    Pretensii = db.Column(db.Text)
    RabWDocs = db.Column(db.Text)
    DateGiveToKom = db.Column(db.Date)


class ConLSH(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Dment = db.Column(db.String(15), nullable=False)
    Dment_en = db.Column(db.String(15))
    Who = db.Column(db.String(15), nullable=False)
    KTRU = db.Column(db.String(20))
    Name = db.Column(db.String(20))
    StageTZ = db.Column(db.Text)
    PlanSrokRazm = db.Column(db.String(15))
    DateSendToKom = db.Column(db.Date)
    DateOfContract = db.Column(db.Date)
    NGosContract = db.Column(db.Integer)
    Organization = db.Column(db.String(15))
    SrokPostavkiPoGK = db.Column(db.Date)
    Pretensii = db.Column(db.Text)
    RabWDocs = db.Column(db.Text)
    DateGiveToKom = db.Column(db.Date)


class ConOMTS(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Dment = db.Column(db.String(15), nullable=False)
    Dment_en = db.Column(db.String(15))
    Who = db.Column(db.String(15), nullable=False)
    KTRU = db.Column(db.String(20))
    Name = db.Column(db.String(20))
    StageTZ = db.Column(db.Text)
    PlanSrokRazm = db.Column(db.String(15))
    DateSendToKom = db.Column(db.Date)
    DateOfContract = db.Column(db.Date)
    NGosContract = db.Column(db.Integer)
    Organization = db.Column(db.String(15))
    SrokPostavkiPoGK = db.Column(db.Date)
    Pretensii = db.Column(db.Text)
    RabWDocs = db.Column(db.Text)
    DateGiveToKom = db.Column(db.Date)


class ConOORSR(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Dment = db.Column(db.String(15), nullable=False)
    Dment_en = db.Column(db.String(15))
    Who = db.Column(db.String(15), nullable=False)
    KTRU = db.Column(db.String(20))
    Name = db.Column(db.String(20))
    StageTZ = db.Column(db.Text)
    PlanSrokRazm = db.Column(db.String(15))
    DateSendToKom = db.Column(db.Date)
    DateOfContract = db.Column(db.Date)
    NGosContract = db.Column(db.Integer)
    Organization = db.Column(db.String(15))
    SrokPostavkiPoGK = db.Column(db.Date)
    Pretensii = db.Column(db.Text)
    RabWDocs = db.Column(db.Text)
    DateGiveToKom = db.Column(db.Date)


class ConOIS(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Dment = db.Column(db.String(15), nullable=False)
    Dment_en = db.Column(db.String(15))
    Who = db.Column(db.String(15), nullable=False)
    KTRU = db.Column(db.String(20))
    Name = db.Column(db.String(20))
    StageTZ = db.Column(db.Text)
    PlanSrokRazm = db.Column(db.String(15))
    DateSendToKom = db.Column(db.Date)
    DateOfContract = db.Column(db.Date)
    NGosContract = db.Column(db.Integer)
    Organization = db.Column(db.String(15))
    SrokPostavkiPoGK = db.Column(db.Date)
    Pretensii = db.Column(db.Text)
    RabWDocs = db.Column(db.Text)
    DateGiveToKom = db.Column(db.Date)


class ConOGE(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Dment = db.Column(db.String(15), nullable=False)
    Dment_en = db.Column(db.String(15))
    Who = db.Column(db.String(15), nullable=False)
    KTRU = db.Column(db.String(20))
    Name = db.Column(db.String(20))
    StageTZ = db.Column(db.Text)
    PlanSrokRazm = db.Column(db.String(15))
    DateSendToKom = db.Column(db.Date)
    DateOfContract = db.Column(db.Date)
    NGosContract = db.Column(db.Integer)
    Organization = db.Column(db.String(15))
    SrokPostavkiPoGK = db.Column(db.Date)
    Pretensii = db.Column(db.Text)
    RabWDocs = db.Column(db.Text)
    DateGiveToKom = db.Column(db.Date)


class ConOOZIS(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Dment = db.Column(db.String(15), nullable=False)
    Dment_en = db.Column(db.String(15))
    Who = db.Column(db.String(15), nullable=False)
    KTRU = db.Column(db.String(20))
    Name = db.Column(db.String(20))
    StageTZ = db.Column(db.Text)
    PlanSrokRazm = db.Column(db.String(15))
    DateSendToKom = db.Column(db.Date)
    DateOfContract = db.Column(db.Date)
    NGosContract = db.Column(db.Integer)
    Organization = db.Column(db.String(15))
    SrokPostavkiPoGK = db.Column(db.Date)
    Pretensii = db.Column(db.Text)
    RabWDocs = db.Column(db.Text)
    DateGiveToKom = db.Column(db.Date)


@login.user_loader
def load_user(id):
    return Users.query.get(int(id))
