from flask import Flask, redirect, render_template, flash
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
    email = StringField(u'邮箱', validators=[DataRequired(message=u'邮箱不能为空'), Length(1, 64), Email(message=u'请输入有效的邮箱地址，比如：username@domain.com')])
    password = StringField(u'密码', validators=[DataRequired(message=u'密码不能为空'), Length(min=5, max=13), AnyOf(['secret', 'password'])])
    submit = SubmitField(u'登录')



@app.route('/submit', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('submit.html', form=form)


@app.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        print("email: %s password: %s" % (email, password))
        print('Form Successfully Submitted!')
        flash(u'登录成功，欢迎回来！', 'info')
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run()