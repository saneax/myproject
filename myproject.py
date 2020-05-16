from flask import Flask, render_template
app = Flask(__name__)

@app.route("/app")
def hello():
    return "<h1 style='color:blue'>Hey! Hello There!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
