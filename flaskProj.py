from flask import Flask, request, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False

@app.route('/', methods=['GET','POST'])
def home():
    return render_template('home.html', form = form)

@app.route('/init', methods=['GET', 'POST'])
def initialize():

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 8080, debug = True)


class FormTwo(FlaskForm):
    name_field = StringField('name')
    fighter_field = IntegerField('Fighter')
    pilot_field = IntegerField('Pilot')
    merchant_field = IntegerField('Merchant')
    engineer_field = IntegerField('Engineer')
    submit = SubmitField('Begin Game')
    select_field = SelectField(u'Difficulty', choices = [('easy', 'easy - 16pts'),('medium','medium - 12pts'),('hard','hard - 8pts')])
