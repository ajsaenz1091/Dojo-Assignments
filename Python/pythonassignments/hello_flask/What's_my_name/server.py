from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def form():
	return render_template("form.html")
@app.route('/process', methods=['post'])
def name():
	print request.form['name']

	return redirect('/')
app.run(debug=True)