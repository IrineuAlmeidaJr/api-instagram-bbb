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
