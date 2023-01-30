from flask import Flask, jsonify

from utils.LoadData import LoadData

app = Flask(__name__)


@app.route("/brothers", methods=['GET'])
def update_data():
    # Aqui não pode ser GET tem que ser um POST que gera um arquivo,
    # o GET que vai ter pega o ultimo arquivo e retorna para o front
    brothers = LoadData.load_data_file()

    lista = [b.__repr__() for b in brothers]

    return jsonify(lista)


if __name__ == '__main__':
    app.run()
