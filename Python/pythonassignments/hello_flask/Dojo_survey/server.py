from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def form():
	return render_template("survey.html")

@app.route('/result',methods=["post"])
def survey():
	name = request.form['name']
	location = request.form['location']
	language = request.form['language']
	comment = request.form['comment']
	return render_template("result.html", name=name, location=location,language=language,comment = comment)

app.run(debug=True)
