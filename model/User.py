import pandas as pd


class User:
    def __init__(self, name, instagram_username, followers, url_image):
        self.__name = name
        self.__instagram_username = instagram_username
        self.__followers = followers
        self.__url_image = url_image

    @property
    def Name(self):
        return self.__name

    @property
    def Instagram_username(self):
        return self.__instagram_username

    @property
    def Followers(self):
        return self.__followers

    @property
    def Url_image(self):
        return self.__url_image

    def __str__(self):
        return f'{self.Name},{self.Instagram_username},' \
               f'{self.Followers},{self.Url_image}'

    def __repr__(self):
        return {
            "name": self.__name,
            "instagram_username": self.__instagram_username,
            "followers": self.__followers,
            "url_image": self.__url_image.rstrip()
        }

    @staticmethod
    def get_all_brothers():
        brothers = []
        with open(f'data/bbb_instagram.txt', "r") as file:
            for item in file:
                if item.strip() != '':
                    brother = item.split(',')
                    brother = User(brother[0], brother[1], int(brother[2]), brother[3])
                    brothers.append(brother)

        brothers = [b.__repr__() for b in brothers]

        return brothers

    @staticmethod
    def get_followers_start():
        # Index in the 'followers_before' variable are the same as in the 'dataset' variable.
        # -> Represents the following that 'brothers' had before entering the BBB
        dataset = pd.read_excel('data/bbb_instagram.xlsx')
        return dataset['2023-01-13'].tolist()

    @staticmethod
    def get_follower_history(name):
        df = pd.read_excel('data/bbb_instagram.xlsx')
        search_name = df[df['Nome'] == name].values.tolist()
        column_names = df.keys().tolist()
        if len(search_name) > 0:
            return {'days': column_names[1:], 'followers': search_name[0][1:]}
        return {'days': [], 'followers': []}

