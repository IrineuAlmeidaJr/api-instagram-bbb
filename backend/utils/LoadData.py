from config.ConfigIntagram import ConfigInstagram
from model.User import User


class LoadData:
    @staticmethod
    def load_data_intagram():
        search_instagram = ConfigInstagram()
        brothers = search_instagram.load()

        return brothers

    @staticmethod
    def load_data_file():
        brothers = []
        with open(f'backup/bbb_instagram_2023-01-27.txt', "r") as file:
            for item in file:
                if item.strip() != '':
                    brother = item.split(',')
                    brother = User(brother[0], brother[1], int(brother[2]), brother[3])
                    brothers.append(brother)
        return brothers
