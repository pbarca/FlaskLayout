from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, RadioField, SelectField
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecret!'


class MyForm(FlaskForm):
    nome = StringField('Nome', validators=[InputRequired()])
    email = StringField('Endereço de Email', validators=[InputRequired()])
    password = PasswordField('Palavra-Passe', validators=[InputRequired()])
    passwordc = PasswordField('Confirme a Palavra-Passe', validators=[InputRequired()])
    textarea = TextAreaField('Textarea')
    radios = RadioField('Radios', default='option1',
                        choices=[('option1', 'Option one is this'), ('option2', 'Option 2 can be something else')])
    selects = SelectField('Select', choices=[('1', '1'), ('2', '2'), ('3', '3')])


@app.route('/', methods=['GET', 'POST'])
def root():
    from datetime import datetime
    horas = datetime.today().hour
    minutos = datetime.today().minute
    segundos = datetime.today().second
    frase1 = ("São {} horas, {} minutos e {} segundos!"
              .format(horas, minutos, segundos))
    if horas < 4:
        frase2 = ('Boa Noite !!!')
    elif horas < 12:
        frase2 = ('Bom Dia !!!')
    elif horas < 20:
        frase2 = ('Boa Tarde !!!')
    else:
        frase2 = ('Boa Noite !!!')
    return render_template('index.html', t1=frase1, t2=frase2)


@app.route('/login', methods=['GET', 'POST'])
def form():
    form = MyForm()

    if form.validate_on_submit():
        return render_template('results.html', email=form.email.data, password=form.password.data,
                               textarea=form.textarea.data, radios=form.radios.data, selects=form.selects.data)
    return render_template('login.html', form=form)


@app.route('/p1')
def p1():
    return render_template('p1.html')


@app.route('/reg', methods=['GET', 'POST'])
def reg():
    form = MyForm()
    return render_template('reg.html', form=form)


@app.route('/p2')
def p2():
    return render_template('p2.html')


@app.route('/p3')
def p3():
    return render_template('p3.html')


if __name__ == '__main__':
    app.run(debug=True)
