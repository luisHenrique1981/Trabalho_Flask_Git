from flask import Flask

app_luis = Flask(__name__)


@app.route("/")
def inicio():
    return "Olá, Turma!"


if __name__ == "__main__":
    app_luis.run(debug=True)