from flask import Flask, render_template, session, redirect,request
app = Flask(__name__)
app.secret_key = "ThisisSecret"

import random

@app.before_first_request
def money():
	session['money'] = 0
	session['activity'] = []

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def money_process():

	if request.form['building'] == "farm":
		random_num = random.randrange(10,20)
		session['money'] += random_num
		session['activity'].append("Ninja guy gainied " +str(random_num) + " from the farm!")
		return redirect('/')

	if request.form['building'] == "cave":
		random_num = random.randrange(5,10)
		session['money'] += random_num
		session['activity'].append("Ninja guy gainied " +str(random_num) + " from the cave!")
		return redirect('/')

	if request.form['building'] == 'house':
		random_num = random.randrange(2,5)
		session['money'] += random_num
		session['activity'].append("Ninja guy gainied " +str(random_num) + " from the house!")
		return redirect('/')

	if request.form['building'] == 'casino':
		random_num = random.randrange(-50,50)
		session['money'] += random_num
		session['activity'].append("Ninja guy gainied " +str(random_num) + " from the house!")
		return redirect('/')


app.run(debug=True)