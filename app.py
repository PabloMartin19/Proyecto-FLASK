from flask import Flask, render_template, request, abort, url_for, redirect
app = Flask(__name__)	

import json
with open('videojuegos.json') as f:
    juegos=json.load(f)
    
@app.before_request
def before_request():
    print('Antes de la petición')

@app.after_request
def after_request(response):
    print('Despues de la petición')
    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route ('/juegos')
def buscar_juego():
    return render_template('juegos.html')


@app.route ('/listajuegos', methods=['POST'])
def listar_juegos():
    nombre_juego = request.form['nombre_juego']
    juegos_filtrados = []
    for juego in juegos:
        if nombre_juego == juego['nombre']:
            juegos_filtrados.append(juego)
    return render_template('listajuegos.html', nombre_juego=nombre_juego, juegos=juegos)

@app.route('/juegos/<nombre_juego>')
def juego(nombre_juego):
    for juego in juegos:
        if juego['nombre'] == nombre_juego:
            return render_template('juego.html', juego=juego)

@app.errorhandler(404)
def error404(error):
    return render_template ('404.html'), 404

app.run("0.0.0.0",30000,debug=True)


