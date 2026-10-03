from flask import Flask, render_template

app_luisHenrique = Flask(__name__, template_folder="templates")

@app_luisHenrique.route("/")
def homepage():
    return render_template("homepage.html")

@app_luisHenrique.route("/contato")
def contato():
    return render_template("contato.html")

if __name__ == "__main__":
    app_luisHenrique.run(port= 8080, debug=True)
    