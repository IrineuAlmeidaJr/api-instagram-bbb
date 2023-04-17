class StatusBrothers:

    def __init__(self):
        self.__leader = 9
        self.__angel = 0
        self.__monster = []
        self.__wall = [8, 10, 20]
        self.__in_game = [3, 5, 8, 9, 10, 17, 20]

    @property
    def Leader(self):
        return self.__leader

    @property
    def Angel(self):
        return self.__angel

    @property
    def Monster(self):
        return self.__monster

    @property
    def Wall(self):
        return self.__wall

    @property
    def In_Game(self):
        return self.__in_game

    def __str__(self):
        return f'{self.Leader}, {self.Angel},{self.Monster},' \
               f'{self.Wall},{self.In_Game}'

    def __repr__(self):
        return {
            "leader": self.Leader,
            "angel": self.Angel,
            "monster": self.Monster,
            "wall": self.Wall,
            "in_game": self.In_Game
        }

