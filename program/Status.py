# Kelas Status
class Status:
    def __init__(self, level=0, maxHP=0, hp=0, atk=0, defense=0):
        self.__level = level
        self.__maxHP = maxHP
        self.__hp = hp              # HP yang dimiliki saat ini, % dari max HP
        self.__atk = atk
        self.__defense = defense

    # Setter
    def set_level(self, level):
        self.__level = level
    
    def set_maxHP(self, maxHP):
        self.__maxHP = maxHP

    def set_hp(self, hp):
        self.__hp = hp

    def set_atk(self, atk):
        self.__atk = atk

    def set_defense(self, defense):
        self.__defense = defense

    # Getter
    def get_level(self):
        return self.__level
    
    def get_maxHP(self):
        return self.__maxHP

    def get_hp(self):
        return self.__hp

    def get_atk(self):
        return self.__atk

    def get_defense(self):
        return self.__defense