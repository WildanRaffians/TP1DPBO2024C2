# Kelas Senjata yang dimiliki Karakter
class Senjata:
    def __init__(self, id="", tipe="", nama="", kenaikanAtk=0, statBonus="", kenaikanStatBonus=0):
        self.__id = id
        self.__tipe = tipe
        self.__nama = nama
        self.__kenaikanAtk = kenaikanAtk             #Jumlah peningkatan ATK, setiap senjata pasti menaikan ATK
        self.__statBonus = statBonus                 #Status bonus (ATK/HP/DEF), setiap senjata berbeda
        self.__kenaikanStatBonus = kenaikanStatBonus #Jumlah peningkatan stat bonus

    # Getter
    def get_id(self):
        return self.__id
    
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
    def set_id(self, id):
        self.__id = id

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