from flask import Flask
from flask import render_template
from flask import request

app=Flask(__name__)
@app.route("/")
def hello(): 
	return "Hello world again."

@app.route("/<name>")
def hello_someone(name):
	return render_template("hello.html", name=name.title())

@app.route("/signup", methods=["POST"])
def sign_up():
	form_data = request.form
	print form_data['name']
	return 'All OK'

if __name__=='__main__':
	app.run(debug=True)
