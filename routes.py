from flask import *
from functools import wraps



app = Flask(__name__)
app.config.from_object(__name__)

app.secret_key = 'KD12J3KMA'


@app.route('/')
def home():
	return render_template('home.html')

@app.route('/contact')
def welcome():
	return render_template('contact.html')


if __name__ == '__main__':
	app.run(debug=True)


