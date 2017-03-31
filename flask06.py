from flask import Flask
from blueprints.blueprint import blueprint

app = Flask(__name__)
app.register_blueprint(blueprint)


@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
