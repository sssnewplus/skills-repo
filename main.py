from flask import Flask

myapp = Flask(__name__)

@myapp.route("/")
def welcome():
	return "<h1>hello from home</h1>"

if __name__ == '__main__':
	myapp.run(debug=True)


