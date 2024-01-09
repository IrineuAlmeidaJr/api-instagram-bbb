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
        with open(f'../data/bbb_instagram.txt', "r") as file:
            for item in file:
                if item.strip() != '':
                    brother = item.split(',')
                    brother = User(brother[0], brother[1].strip(), brother[2], int(brother[3]), brother[4])
                    brothers.append(brother)
        return brothers
