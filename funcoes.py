import os
import requests


def ntf_img():
    with os.scandir('static/images') as dir:
        qtm_qtd = 0
        for arq in dir:
            if arq.name.startswith('questionmark'):
                qtm_qtd += 1
    return qtm_qtd


def poke_cor(jsn):
    color = jsn['color']['name']
    return dic_cores[color], jsn['color']['name']


def tipos_do_pokemon(jsn):
    lista = []
    for item in jsn['types']:
        lista.append(item['type']['name'])
    tipos = []
    for item in lista:
        tipos.append(dic_tipos[item])
    return tipos


def evolucao_anterior(jsn):
    if jsn['evolves_from_species'] == None:
        return None
    else:
        return jsn['evolves_from_species']['name']


def proximas_evolucoes(jsn):
    nome = jsn['name']
    url = jsn['evolution_chain']['url']
    retorno = requests.get(url)
    retorno = retorno.json()['chain']
    lista = []
    if retorno['species']['name'] != nome:
        for indice in retorno['evolves_to']:
            if indice['species']['name'] == nome:
                retorno = indice
                break
            for item in indice['evolves_to']:
                if item['species']['name'] == nome:
                    retorno = item
                    break
    if retorno['evolves_to'] == []: 
        return lista
    else:
        for i in retorno['evolves_to']:
            lista.append(i['species']['name'])
        return lista


def filtro_json_pokemon(jsn, jsn_evo):
    cor = poke_cor(jsn_evo)
    tipos = tipos_do_pokemon(jsn)
    evol_anterior = evolucao_anterior(jsn_evo)
    evol_posteriores = proximas_evolucoes(jsn_evo)
    dic = {
        'id': jsn['id'],
        'nome': jsn['name'],
        'altura': jsn['height'],
        'peso': jsn['weight'],
        'imagem': jsn['sprites']['other']['official-artwork']['front_default'],
        'cor': cor,
        'tipos': tipos,
        'evol_anterior': evol_anterior,
        'evol_posteriores': evol_posteriores
        }
    return dic


dic_cores = {
    "brown": "marrom",
    "yellow": "amarelo",
    "blue": "azul",
    "pink": "rosa",
    "gray": "cinza",
    "purple": "roxo",
    "red": "vermelho",
    "white": "branco",
    "green": "verde",
    "black": "preto"
}

dic_tipos = {
    "normal": "normal",
    "fighting": "lutador",
    "flying": "voador",
    "poison": "veneno",
    "ground": "terra",
    "rock": "pedra",
    "bug": "inseto",
    "ghost": "fantasma",
    "steel": "aço",
    "fire": "fogo",
    "water": "água",
    "grass": "grama",
    "electric": "elétrico",
    "psychic": "psíquico",
    "ice": "gelo",
    "dragon": "dragão",
    "dark": "noturno",
    "fairy": "fada"
}