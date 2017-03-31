from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/hello/<username>")
def hello_someone(username):
    return "Hello " + username + "!"


# or use <converter:variable_name>
@app.route("/converted/<string:username>")
def hello_converted_someone(username):
    return "Welcome converted: " + username + "!"

if __name__ == "__main__":
    app.run()
