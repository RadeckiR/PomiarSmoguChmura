from flask import Flask
app = Flask(__name__)




@app.route("/")
def index():
    return "witamy na aplikacji pokazującej stan powietrza w twojej okolicy"


@app.route("/pogoda/")
def who():
    return "stan dzisiejszej pogody:"


@app.route("/hi/<username>")
def greet(username):
    return f"hi there, {username}"
if __name__ == "__main__":
    app.run()


