from flask import Flask, render_template

app_luisHenrique = Flask(__name__, template_folder="templates")



@app_luisHenrique.route("/ola")
def raiz():
    return f"Ola, Turma"

def saudacoes(nome):
    return f"Ola, {nome}"


if __name__ == "__main__":
    app_luisHenrique.run(port= 8080, debug=True)