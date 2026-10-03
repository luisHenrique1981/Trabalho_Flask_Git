from flask import Flask, render_template, request

app_luisHenrique = Flask(__name__, template_folder="t_templates")

@app_luisHenrique.route("/")
@app_luisHenrique.route("/index")
def indice():
    return render_template("t_index.html")

@app_luisHenrique.route("/contato")
def contato():
    return render_template("t_contato.html")

@app_luisHenrique.route("/login")
def login():
    return render_template("t_login.html")

@app_luisHenrique.route("/autenticar", methods=['GET', 'POST'])
def autenticar():
    usuario = request.args.get('nome_usuario')
    senha = request.args.get('senha')
    return f"usuario: {usuario} e senha: {senha}"

@app_luisHenrique.route("/usuario", defaults={"nome_usuario": "usuario?", "nome_profissao": ""})
def usuarios(nome_usuario, nome_profissao):
    dados_usu = {"profissao": nome_profissao, "disciplina": "Desenvolvimento Web III"}
    return render_template("t_usuario.html", nome=nome_usuario, dados=dados_usu)

if __name__ == "__main__":
    app_luisHenrique.run(port= 8080, debug=True)
