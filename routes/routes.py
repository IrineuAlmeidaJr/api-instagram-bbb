from app import app

from controllers import user_controller, news_controller


# Brothers
@app.route("/brothers", methods=['GET'])
def get_all_brothers():
    return user_controller.get_all_brothers()


@app.route("/brother/compare-followers", methods=['GET'])
def get_compare_followers():
    return user_controller.get_compare_followers()


@app.route("/brother/<string:name>", methods=['GET'])
def get_follower_history_brother(name):
    return user_controller.get_follower_history_brother(name)


@app.route("/ranking", methods=["GET"])
def get_ranking_brothers():
    return user_controller.get_ranking_brothers()


# News
@app.route("/news", methods=["GET"])
def get_news():
    return news_controller.get_news()
