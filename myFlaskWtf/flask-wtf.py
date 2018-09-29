
from flask import Flask, redirect, render_template, flash,url_for
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length,Email,AnyOf
from flask_bootstrap import Bootstrap
app=Flask(__name__)
Bootstrap(app)
app.secret_key = '1234567'

class MyForm(FlaskForm):
    user = StringField('Username', validators=[DataRequired()])

class LoginForm(FlaskForm):
    name = StringField(u'姓名', validators=[DataRequired(message=u'姓名不能为空'), Length(1, 64)])
    way = StringField(u'假期去向', validators=[DataRequired(message=u'假期去向不能为空'), Length(1, 128)])
    time= StringField(u'离返校时间')
    submit = SubmitField(u'登录')


@app.route('/')#首页
def index():
    login_url=url_for('login')
    return redirect(login_url)#重定向为登录页面
    return u'这是首页'

@app.route('/submit', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('submit.html', form=form)

def writeFile(s):
    with open('result.log','a') as fw:
        fw.write(s)

result=[]
@app.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        name = form.name.data
        way = form.way.data
        time = form.time.data
        print("name: %s way: %s time:%s" % (name, way,time))
        writeFile(name+'\t'+way+'\t'+time+'\n')
        flash(u'感谢填写','info')
    return render_template('login.html',form=form)

if __name__ == '__main__':
    app.run()





