import pandas as pd
import numpy as np


class User:

    def __init__(self, id, name, instagram_username, followers, url_image):
        self.__id = id
        self.__name = name
        self.__instagram_username = instagram_username
        self.__followers = followers
        self.__url_image = url_image

    @property
    def Id(self):
        return self.__id

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
        return f'{self.Id}, {self.Name},{self.Instagram_username},' \
               f'{self.Followers},{self.Url_image}'

    def __repr__(self):
        return {
            "id": self.Id,
            "name": self.Name,
            "instagram_username": self.Instagram_username,
            "followers": self.Followers,
            "url_image": self.Url_image.rstrip()
        }

    @staticmethod
    def __order_brothers(in_game):
        in_game = np.array(in_game)
        brothers = []
        with open(f'data/bbb_instagram.txt', "r") as file:
            for item in file:
                if item.strip() != '':
                    brother = item.split(',')
                    brother = User(int(brother[0]), brother[1], brother[2], int(brother[3]), brother[4])
                    brothers.append(brother)

        brothers_in_game = [temp_brother for temp_brother in brothers if temp_brother.Id in in_game]
        brothers_not_in_game = [temp_brother for temp_brother in brothers if temp_brother.Id not in in_game]
        return brothers_in_game + brothers_not_in_game

    @staticmethod
    def get_all_brothers(in_game):
        brothers = User.__order_brothers(in_game)
        brothers = [b.__repr__() for b in brothers]

        return brothers

    @staticmethod
    def get_followers_start(in_game):
        # Index in the 'followers_before' variable are the same as in the 'dataset' variable.
        # -> Represents the following that 'brothers' had before entering the BBB
        dataset = pd.read_excel('data/bbb_instagram.xlsx')

        brothers = User.__order_brothers(in_game)

        ids_brothers = np.array([brother.Id for brother in brothers])

        lista = []
        df = dataset[['Id', '2023-01-13']]
        for id_brother in ids_brothers:
            lista.append(int(df[df['Id'] == id_brother]['2023-01-13'].values))

        return lista

    @staticmethod
    def get_follower_history(name):
        name = str(name).strip()
        df = pd.read_excel('data/bbb_instagram.xlsx')
        followers = df[df['Nome'] == name].values.tolist()[0][2:]
        column_names = df.keys().tolist()

        if len(followers) > 0:
            return {
                'text': {
                    'days': column_names[2:],
                    'followers': [int(follower) for follower in followers]
                },
                'chart': {
                    'days': column_names[2:],
                    'followers': [int(follower / 1000) for follower in followers]
                }
            }
        return {'days': [], 'followers': []}

    @staticmethod
    def get_ranking():
        df = pd.read_excel('data/bbb_instagram.xlsx')
        df_column_names = df.keys().to_numpy()
        url_brothers_image = pd.DataFrame(np.loadtxt('image/url_imagens_brothers.txt', dtype=str))

        name_followers = df[[df_column_names[1], df_column_names[-1]]]
        name_followers['url_image'] = url_brothers_image

        name_followers = name_followers.sort_values(df_column_names[-1], ascending=False)

        user_local = []
        for index, row in name_followers.iterrows():
            user_local.append({
                'name': row['Nome'],
                'followers': row[df_column_names[-1]],
                'url_image': row['url_image']
            })

        return user_local

    @staticmethod
    def get_compare_followers():
        df = pd.read_excel('data/bbb_instagram.xlsx')
        url_brothers_image = np.loadtxt('image/url_imagens_brothers.txt', dtype=str)
        brothers = []
        columns_names = df.columns.tolist()

        if len(df.columns) >= 4:
            list_for_compare = df[[
                columns_names[0],
                columns_names[1],
                columns_names[-2],
                columns_names[-1]
            ]]

            for index, row in list_for_compare.iterrows():
                brothers.append({
                    'name': row[1],
                    'url_image': url_brothers_image[index],
                    'new_followers': row[-1] - row[-2]
                })

        return brothers
