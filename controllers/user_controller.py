import pandas as pd
from flask import jsonify, request

from model.User import User
from model.StatusBrothers import StatusBrothers


def get_all_brothers():
    status_brothers = StatusBrothers(
        id_brother_leader=6,
        id_brother_angel=16,
        ids_brothers_monster=[],
        ids_brothers_wall=[4, 18, 19],
        ids_brothers_in_game=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                              13, 14, 16, 17, 18, 19, 20, 21, 22]
    )
    brothers = User.get_all_brothers(status_brothers.In_Game)
    followers_before = User.get_followers_start(status_brothers.In_Game)

    return jsonify({
        'brothers': brothers,
        'followers_before': followers_before,
        'status_brothers': status_brothers.__repr__()
    })


def get_follower_history_brother(name):
    return jsonify(User.get_follower_history(name))


def get_ranking_brothers():
    return jsonify(User.get_ranking())
