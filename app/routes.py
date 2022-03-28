from flask import render_template, flash, redirect, url_for, send_from_directory
from app import app
from flask_login import current_user, login_user
from app.models import Users, ConOIS, ConLSH, ConOGE, ConPTV, ConOMTS, ConOORSR, ConOOZIS
from flask_login import logout_user, login_required
from flask import request
from werkzeug.urls import url_parse
from app import db
from app.forms import RegistrationForm, ChangeDmentForm, LoginForm, AddContract, ShowConForm, EditConForm
from datetime import datetime, date, timedelta
import os
import config
from sqlalchemy.sql import select, and_, or_, not_, text


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Неправильное имя пользователя или пароль!')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sing In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET','POST'])
@login_required
def register():
    if current_user.Dment != "admin":
        return redirect(url_for('noperm'))#nopermission if not admin
    form = RegistrationForm()
    if form.validate_on_submit():
        user = Users(username=form.username.data, Dment=form.dment.data, Dment_RU=form.dment_RU.data, FIO=form.fio.data, Dment_head=form.dm_Head.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Пользователь зарегестрирован!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/user/<username>')
@login_required
def user(username):
    user = Users.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)


@app.route('/ct/<dment>/<cnum>', methods=['GET','POST'])
@login_required
def ct(dment, cnum):
    form = ShowConForm()
    contract = None

    if dment != current_user.Dment and current_user.Dment != "SVOD":
        return redirect(url_for('noperm'))

    if dment == "OIS":
        contract = ConOIS.query.filter_by(id=cnum).first_or_404()
    elif dment == "PTV":
        contract = ConPTV.query.filter_by(id=cnum).first_or_404()
    elif dment == "LSH":
        contract = ConLSH.query.filter_by(id=cnum).first_or_404()
    elif dment == "OMTS":
        contract = ConOMTS.query.filter_by(id=cnum).first_or_404()
    elif dment == "OORSR":
        contract = ConOORSR.query.filter_by(id=cnum).first_or_404()
    elif dment == "OGE":
        contract = ConOGE.query.filter_by(id=cnum).first_or_404()
    elif dment == "OOZIS":
        contract = ConOOZIS.query.filter_by(id=cnum).first_or_404()
    elif dment == "SVOD" or dment == "admin":
        if dment == "OIS":
            contract = ConOIS.query.filter_by(id=cnum).first_or_404()
        elif dment == "PTV":
            contract = ConPTV.query.filter_by(id=cnum).first_or_404()
        elif dment == "LSH":
            contract = ConLSH.query.filter_by(id=cnum).first_or_404()
        elif dment == "OMTS":
            contract = ConOMTS.query.filter_by(id=cnum).first_or_404()
        elif dment == "OORSR":
            contract = ConOORSR.query.filter_by(id=cnum).first_or_404()
        elif dment == "OGE":
            contract = ConOGE.query.filter_by(id=cnum).first_or_404()
        elif dment == "OOZIS":
            contract = ConOOZIS.query.filter_by(id=cnum).first_or_404()

    form.Dment.data = contract.Dment
    form.Who.data = contract.Who
    form.KTRU.data = contract.KTRU
    form.Name.data = contract.Name
    form.StageTZ.data = contract.StageTZ
    form.PlanSrokRazm.data = contract.PlanSrokRazm
    form.DateSendToKom.data = contract.DateSendToKom
    form.DateOfContract.data = contract.DateOfContract
    form.NGosContract.data = contract.NGosContract
    form.Organization.data = contract.Organization
    form.SrokPostavkiPoGK.data = contract.SrokPostavkiPoGK
    form.Pretensii.data = contract.Pretensii
    form.RabWDocs.data = contract.RabWDocs
    form.DateGiveToKom.data = contract.DateGiveToKom

    if form.validate_on_submit():
        return redirect(url_for('razrab'))

    return render_template('ct.html', form=form, title='Просмотр контракта', items=contract)


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.now() #.strftime('%d/%m/%Y %H:%M:%S')
        db.session.commit()

@app.route('/changedment')
def changedment():
    if current_user.Dment != 'admin':
        return redirect(url_for('noperm'))
    form = ChangeDmentForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first_or_404()
        user.Dment = form.NewDment.data
        db.session.commit()
    return render_template('changedment.html', title='Смена отдела', form=form)

@app.route('/about', methods=['GET','POST'])
def about():
    return render_template('about.html', title='Информация')


def date_str_to_obj(inputdate):
    reciveddate = inputdate.split('.')
    outputdate = date(int(reciveddate[2]), int(reciveddate[1]), int(reciveddate[0]))
    return outputdate


@app.route('/addcontract', methods=['GET','POST'])
@login_required
def addcontract():
    form = AddContract()
    if form.validate_on_submit():
        #date_plansrokrazm_out = date_str_to_obj(form.PlanSrokRazm.data) убрано т.к. вносится строка перенести в ConEditFunction
        #date_sendtokom_out = date_str_to_obj(form.DateSendToKom.data)
        #date_ofcontract_out = date_str_to_obj(form.DateOfContract.data)
        #date_srokpostavki_out = date_str_to_obj(form.SrokPostavkiPoGK.data)
        #date_givetokom_out = date_str_to_obj(form.DateGiveToKom.data)
        if current_user.Dment == "OIS":
            contract = ConOIS(Dment=current_user.Dment_RU, Dment_en=current_user.Dment, Who=current_user.FIO, StageTZ=form.StageTZ.data, KTRU=form.KTRU.data, Name=form.Name.data, PlanSrokRazm=form.PlanSrokRazm.data)
        elif current_user.Dment == "PTV":
            contract = ConPTV(Dment=current_user.Dment_RU, Dment_en=current_user.Dment, Who=current_user.FIO, StageTZ=form.StageTZ.data, KTRU=form.KTRU.data, Name=form.Name.data, PlanSrokRazm=form.PlanSrokRazm.data)
        elif current_user.Dment == "LSH":
            contract = ConLSH(Dment=current_user.Dment_RU, Dment_en=current_user.Dment, Who=current_user.FIO, StageTZ=form.StageTZ.data, KTRU=form.KTRU.data, Name=form.Name.data, PlanSrokRazm=form.PlanSrokRazm.data)
        elif current_user.Dment == "OMTS":
            contract = ConOMTS(Dment=current_user.Dment_RU, Dment_en=current_user.Dment, Who=current_user.FIO, StageTZ=form.StageTZ.data, KTRU=form.KTRU.data, Name=form.Name.data, PlanSrokRazm=form.PlanSrokRazm.data)
        elif current_user.Dment == "OORSR":
            contract = ConOORSR(Dment=current_user.Dment_RU, Dment_en=current_user.Dment, Who=current_user.FIO, StageTZ=form.StageTZ.data, KTRU=form.KTRU.data, Name=form.Name.data, PlanSrokRazm=form.PlanSrokRazm.data)
        elif current_user.Dment == "OGE":
            contract = ConOGE(Dment=current_user.Dment_RU, Dment_en=current_user.Dment, Who=current_user.FIO, StageTZ=form.StageTZ.data, KTRU=form.KTRU.data, Name=form.Name.data, PlanSrokRazm=form.PlanSrokRazm.data)
        elif current_user.Dment == "OOZIS":
            contract = ConOOZIS(Dment=current_user.Dment_RU, Dment_en=current_user.Dment, Who=current_user.FIO, StageTZ=form.StageTZ.data, KTRU=form.KTRU.data, Name=form.Name.data, PlanSrokRazm=form.PlanSrokRazm.data)
        else:
            flash('Вы не можете добавить контракт!')
            return redirect(url_for('addcontract'))
        db.session.add(contract)
        db.session.commit()
        flash('Контракт добавлен!')
        return redirect(url_for('addcontract'))
    return render_template('addcontract.html', title='Новый контракт', form=form)


@app.route('/conlist', methods=['GET','POST'])
@login_required
def conlist():
    if current_user.Dment == "OIS":
        if current_user.Dment_head:
            items = ConOIS.query.all()
        else:
            items = ConOIS.query.filter_by(Who=current_user.FIO)
    elif current_user.Dment == "PTV":
        if current_user.Dment_head:
            items = ConPTV.query.all()
        else:
            items = ConPTV.query.filter_by(Who=current_user.FIO)
    elif current_user.Dment == "LSH":
        if current_user.Dment_head:
            items = ConLSH.query.all()
        else:
            items = ConLSH.query.filter_by(Who=current_user.FIO)
    elif current_user.Dment == "OMTS":
        if current_user.Dment_head:
            items = ConOMTS.query.all()
        else:
            items = ConOMTS.query.filter_by(Who=current_user.FIO)
    elif current_user.Dment == "OORSR":
        if current_user.Dment_head:
            items = ConOORSR.query.all()
        else:
            items = ConOORSR.query.filter_by(Who=current_user.FIO)
    elif current_user.Dment == "OGE":
        if current_user.Dment_head:
            items = ConOGE.query.all()
        else:
            items = ConOGE.query.filter_by(Who=current_user.FIO)
    elif current_user.Dment == "OOZIS":
        if current_user.Dment_head:
            items = ConOOZIS.query.all()
        else:
            items = ConOOZIS.query.filter_by(Who=current_user.FIO)
    elif current_user.Dment == "SVOD" or current_user.Dment == "admin":
        p1 = db.session.query(ConOIS)
        p2 = db.session.query(ConPTV)
        p3 = db.session.query(ConLSH)
        p4 = db.session.query(ConOMTS)
        p5 = db.session.query(ConOORSR)
        p6 = db.session.query(ConOGE)
        p7 = db.session.query(ConOOZIS)
        items = p1.union_all(p2).union_all(p3).union_all(p4).union_all(p5).union_all(p6).union_all(p7)
    else:
        return redirect(url_for('noperm'))
    datetd = date.today()
    warndate = datetd - timedelta(3)
    delta = timedelta(3)
    return render_template('conlist.html', items=items, datetd=datetd, warndate=warndate, delta=delta)


@app.route('/userlist', methods=['GET', 'POST'])
@login_required
def userlist():
    if current_user.Dment != "admin":
        return redirect(url_for('noperm'))  # nopermission if not admin
    items = Users.query.all()
    return render_template('userlist.html', items=items)


@app.route('/noperm')
def noperm():
    return render_template('noperm.html')


@login_required
@app.route('/razrab')
def razrab():
    return render_template('razrab.html')