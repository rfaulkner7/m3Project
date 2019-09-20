from flask import Flask, request, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False


@app.route('/', methods=['GET', 'POST'])
def home():
    form = HomeForm()
    if form.is_submitted():
        return redirect("http://127.0.0.1:8080/init", code=302)
    return render_template('home.html', form=form)


class HomeForm(FlaskForm):
    input_field = StringField('Input')
    submit = SubmitField('Start')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
