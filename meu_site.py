from flask import Flask, render_template

app = Flask(__name__)

@app.route("/página")
def pagina():
    return render_template("página.html")

@app.route("/membros")
def membros():
    return render_template("membros.html")

@app.route("/usuarios/<nome_usuario>")
def usuario(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

if __name__ == "__main__":
    app.run(debug=True)









