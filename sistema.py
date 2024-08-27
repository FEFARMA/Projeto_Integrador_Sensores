from flask import Flask, jsonify, make_response, request
# Importa o banco de dados
from bd import Sensores

# Instanciar o modulo Flask na nossa variavel app
app = Flask('sensores')

# PRIMEIRO METODO - VISUALIZAR OS DADOS (GET)
# app.route -> definir que essa funcao e uma rota que o flask entenda que aquilo e um metodo que deve ser executado
@app.route('/sensores', methods=['GET'])
def get_sensores():
    return Sensores

# PRIMEIRO METODO PARTE 2 - VISUALIZAR DADOS POR ID (GET / ID)
@app.route('/sensores/<int:id>', methods=['GET'])
def get_sensores_id(id):
    for sensores in Sensores:
        if sensores.get('id') == id:
            return jsonify(sensores)
        
# SEGUNDO METODO - CRIAR NOVOS DADOS (POST)
@app.route('/sensores', methods=['POST'])
def criar_sensores():
    sensores = request.json
    Sensores.append(sensores)
    return make_response(
        jsonify(mensagem='Medição cadastrada com sucesso', 
                sensores=sensores
                )
    )

# TERCEIRO METODO - EDITAR DADOS (PUT)
@app.route('/sensores/<int:id>', methods=['PUT'])
def editar_sensores_id(id):
    sensor_alterado = request.get_json()
    for indice, sensores in enumerate(Sensores):
        if sensores.get('id') == id:
            Sensores[indice].update(sensor_alterado)
            return jsonify(Sensores[indice])


# QUARTO METODO - DELETAR DADOS (DELETE)
@app.route('/sensores/<int:id>', methods=['DELETE'])
def excluir_sensor(id):
    for indice, sensores in enumerate(Sensores):
        if sensores.get('id') == id:
            del Sensores[indice]
            return jsonify({"mensagem:": "Medição excluida com Sucess0"})
    



app.run(port=5000, host='localhost')        



        
