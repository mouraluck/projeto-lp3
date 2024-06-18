from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    lista_produtos = [
    {"nome": "AmbientChá", "desc": "Este chá é milagroso", "img": "1"},
    {"nome": "CanabCreme", "desc": "Este creme é milagroso", "img": "2"},
    {"nome": "VerdeGel", "desc": "Este gel é milagroso", "img": "3"},
    {"nome": "GreenPlant", "desc": "Esta planta é milagrosa", "img": "4"},
    {"nome": "PoliVita", "desc": "Este polivitaminico é milagroso", "img": "5"},
    {"nome": "NatureLive", "desc": "Este produto é milagroso", "img": "6"},
    ]
    return render_template('index.html', produtos=lista_produtos)

@app.route('/carrinho')
def carrinho():
    return render_template('../static/assets/html/carrinho.html')
