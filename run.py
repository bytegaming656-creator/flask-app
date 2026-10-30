from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello This is main route"
@app.route("/about")
def abt():
    return "This is about page"

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True,port=8080)
