from flask import render_template, Flask

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
# if __name__ == '__main__':
#    app.run(host="localhost", port=8000, debug=True)
