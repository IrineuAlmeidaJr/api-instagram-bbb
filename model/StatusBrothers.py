class StatusBrothers:

    def __init__(self, id_brother_leader, id_brother_angel, ids_brothers_monster,
                 ids_brothers_wall, ids_brothers_in_game):
        self.__leader = id_brother_leader
        self.__angel = id_brother_angel
        self.__monster = ids_brothers_monster
        self.__wall = ids_brothers_wall
        self.__in_game = ids_brothers_in_game

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

