from flask import Flask
#from validate_docbr import CPF
app = Flask("Minha aplicação")

@app.route("/")
def home():
    return '<h1>Home page</h1><a href="/contact"<h1>Outra pagina</h1></a>'

@app.route("/contact")
def contact():
    return "<h1>Contato</h1>"

@app.route("/product")
def product():
    return "<h1>Produtos<h1/>"