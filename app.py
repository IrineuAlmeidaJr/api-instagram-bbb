from flask import Flask, jsonify
import pandas as pd

from utils.LoadData import LoadData

app = Flask(__name__)


@app.route("/brothers", methods=['GET'])
def update_data():
    brothers = LoadData.load_data_file()

    brothers = [b.__repr__() for b in brothers]

    # Index in the 'followers_before' variable are the same as in the 'dataset' variable.
    # -> Represents the following that 'brothers' had before entering the BBB
    dataset = pd.read_excel('data/bbb_instagram.xlsx')
    followers_before = dataset['2023-01-13'].tolist()

    return jsonify({'brothers': brothers, 'followers_before': followers_before})


if __name__ == '__main__':
    app.run()
