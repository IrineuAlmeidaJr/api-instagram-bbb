import pandas as pd
from flask import jsonify, request

from model.User import User
from model.StatusBrothers import StatusBrothers


def get_all_brothers():
    status_brothers = StatusBrothers()
    brothers = User.get_all_brothers(status_brothers.In_Game)
    followers_before = User.get_followers_start(status_brothers.In_Game)

    return jsonify({
        'brothers': brothers,
        'followers_before': followers_before,
        'status_brothers': status_brothers.__repr__()
    })


def get_compare_followers():
    status_brothers = StatusBrothers()
    brothers = User.get_compare_followers(status_brothers.In_Game)
    followers_before = User.get_followers_start(status_brothers.In_Game)
    return jsonify({
        'brothers': brothers,
        'followers_before': followers_before,
        'status_brothers': status_brothers.__repr__()
    })
    # return jsonify()


def get_follower_history_brother(name):
    return jsonify(User.get_follower_history(name))


def get_ranking_brothers():
    return jsonify(User.get_ranking())
