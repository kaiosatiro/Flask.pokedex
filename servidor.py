from flask import Flask, request, render_template, url_for
import requests
from random import randint
import funcoes

app = Flask(__name__)

@app.route("/", methods=["GET"])
@app.route("/form", methods=["GET"])
def hello():
    return render_template("form.html")

@app.route("/pesquisa", methods=["POST", "GET"])
def consulta_pokemon():
    nome_id = request.form['nome_id']
    consulta = requests.get(f'https://pokeapi.co/api/v2/pokemon/{nome_id.lower()}/')
    if consulta.status_code == 404:
        i = randint(1, qtm_qtd+1)
        img = f'images/questionmark({i}).png'
        return render_template('not_found.html', img= img)
    else:
        consulta_evol = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{nome_id.lower()}')
        dic = funcoes.filtro_json_pokemon(consulta.json(), consulta_evol.json())
        return render_template('pokemon.html', **dic)

qtm_qtd = funcoes.ntf_img()

if __name__ == '__main__':
    app.run(host = 'localhost', port = 5002, debug = True)
