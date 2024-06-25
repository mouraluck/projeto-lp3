from flask import Flask, render_template ,request

app = Flask(__name__)
lista_produtos = [
{"nome": "AmbientChá", "desc": "Este chá é milagroso", "img": "1"},
{"nome": "CanabCreme", "desc": "Este creme é milagroso", "img": "2"},
{"nome": "VerdeGel", "desc": "Este gel é milagroso", "img": "3"},
{"nome": "GreenPlant", "desc": "Esta planta é milagrosa", "img": "4"},
{"nome": "PoliVita", "desc": "Este polivitaminico é milagroso", "img": "5"},
{"nome": "NatureLive", "desc": "Este produto é milagroso", "img": "6"},
    ]
@app.route('/')
def home():

    return render_template('index.html', produtos=lista_produtos)

@app.route('/carrinho')
def carrinho():
    return render_template('carrinho.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/cadastro' ,methods=['post'])
def cadastro_produtos():
    nome = request.form['nome'] #dicionario
    descricao = request.form['descricao']
    produto = { 'nome': nome, 'descricao': descricao, 'img':''}
    lista_produtos.append(produto)
    return render_template('index.html', produtos=lista_produtos)