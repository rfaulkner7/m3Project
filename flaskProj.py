from flask import Flask, request, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False
name = "char"
difficulty = "easy"
fighter = 0
pilot = 0
merchant = 0
engineer = 0
credits = 0

@app.route('/', methods=['GET', 'POST'])
def home():
    form = HomeForm()
    if form.is_submitted():
        return redirect("http://127.0.0.1:8080/init", code=302)
    else:
        return render_template('home.html', form = form)

@app.route('/init', methods=['GET', 'POST'])
def initialize():
    form = ConfigForm()
    global name
    global difficulty
    global fighter
    global pilot
    global merchant
    global engineer
    global credits

    if form.is_submitted():
        difficulty = form.select_field.data
        name = form.name_field.data
        try:
            fighter = int(form.fighter_field.data)
        except:
            fighter = 0
        try:
            pilot = int(form.pilot_field.data)
        except:
            pilot = 0
        try: 
            merchant = int(form.merchant_field.data)
        except:
            merchant = 0
        try:
            engineer = int(form.engineer_field.data)
        except:
            engineer = 0

        total = fighter+pilot+merchant+engineer

        if difficulty == "easy" and total == 16 :
            credits = 1000
            return redirect("http://127.0.0.1:8080/display", code=302)
        elif difficulty == "medium" and total == 12 :
            credits = 500
            return redirect("http://127.0.0.1:8080/display", code=302)
        elif difficulty == "hard" and total == 8 :
            credits = 100
            return redirect("http://127.0.0.1:8080/display", code=302)
        else:
            return render_template("game.html", form = form, status = "incorrect point allocation!")
    else: 
        return render_template("game.html", form = form, status = '')

@app.route('/display', methods=['GET', 'POST'])
def display():
    global name
    global difficulty
    global fighter
    global pilot
    global merchant
    global engineer
    global credits

    return render_template('display.html', difficulty=difficulty, name = name, fighter = fighter, pilot = pilot, merchant = merchant, engineer = engineer, credits = credits)

class HomeForm(FlaskForm):
    submit = SubmitField('Start')

class ConfigForm(FlaskForm):
    name_field = StringField('name')
    fighter_field = IntegerField('Fighter')
    pilot_field = IntegerField('Pilot')
    merchant_field = IntegerField('Merchant')
    engineer_field = IntegerField('Engineer')
    submit = SubmitField('Begin Game')
    select_field = SelectField(u'Difficulty', choices = [('easy', 'easy - 16pts'),('medium','medium - 12pts'),('hard','hard - 8pts')])

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 8080, debug = True)