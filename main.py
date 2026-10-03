from flask import Flask, render_template

app_luisHenrique = Flask(__name__, template_folder="templates")

@app_luisHenrique.route("/")
@app_luisHenrique.route("/rota1")
def rota1():
    return f"Ola, Turma"

@app_luisHenrique.route("/rota2")
def rota2():
    resposta = "<H3> Essa é a outra página da rota 2<H3>"
    return resposta

def saudacoes(nome):
    return f"Ola, {nome}"

if __name__ == "__main__":
    app_luisHenrique.run(port= 8080, debug=True)