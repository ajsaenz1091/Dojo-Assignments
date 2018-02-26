from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def noninjas():
	return render_template('noninjas.html')
@app.route('/ninja')
def ninja():
	return render_template('ninjas.html')


@app.route('/ninja/<color>')
def ninja_color(color):
	if (color == 'purple'):
		return render_template('purple.html')
	elif (color == 'blue'):
		return render_template('blue.html')
	elif (color == 'orange'):
		return render_template('orange.html')
	elif (color == 'red'):
		return render_template('red.html')
	else:
		return render_template('notapril.html')

app.run(debug=True)
