from flask import jsonify

from model.News import News


def get_news():
    return jsonify([news.__repr__() for news in News.get_news()])
