from flask import Flask
app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
@app.route("/hello")
def hello_world():
	return "Hello, world! I'm I."

@app.route("/test/<search_query>")
def search(search_query):
	return search_query

@app.route("/name/<name>")
def index(name):
	if name=="michael":
		return "Hello, {}".format(name), 200
	else:
		return "Not Found", 404

if __name__ == "__main__":
	app.run()