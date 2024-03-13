class Senjata:
    __tipe = ""
    __nama = ""
    __kenaikanAtk = 0
    __statBonus = ""
    __kenaikanStatBonus = 0
    

    def __init__(self, tipe="", nama="", kenaikanAtk=0, statBonus="", kenaikanStatBonus=0):
        self.__tipe = tipe
        self.__nama = nama
        self.__kenaikanAtk = kenaikanAtk
        self.__statBonus = statBonus
        self.__kenaikanStatBonus = kenaikanStatBonus

    # Getter
    def get_tipe(self):
        return self.__tipe

    def get_nama(self):
        return self.__nama

    def get_kenaikanAtk(self):
        return self.__kenaikanAtk

    def get_statBonus(self):
        return self.__statBonus

    def get_kenaikanStatBonus(self):
        return self.__kenaikanStatBonus

    # Setter
    def set_tipe(self, tipe):
        self.__tipe = tipe

    def set_nama(self, nama):
        self.__nama = nama

    def set_kenaikanAtk(self, kenaikanAtk):
        self.__kenaikanAtk = kenaikanAtk

    def set_statBonus(self, statBonus):
        self.__statBonus = statBonus

    def set_kenaikanStatBonus(self, kenaikanStatBonus):
        self.__kenaikanStatBonus = kenaikanStatBonus