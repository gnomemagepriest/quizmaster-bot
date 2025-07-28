from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def greet():
    return "<h1>Hello world.</h1>"

if __name__ == "__main__":
    app.run(debug=True)