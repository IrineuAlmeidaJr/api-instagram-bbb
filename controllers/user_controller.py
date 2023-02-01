import pandas as pd
from model.User import User
from flask import jsonify, request


def get_all_brothers():
    brothers = User.get_all_brothers()
    followers_before = User.get_followers_start()
    return jsonify({'brothers': brothers, 'followers_before': followers_before})


def get_follower_history_brother(name):
    return jsonify(User.get_follower_history(name))
