# Kelas Wilayah
class Wilayah:
    def __init__(self, nama="", deskripsi="", item=[], niceNpc=[], enemyNpc=[]):
        self.__nama = nama
        self.__deskripsi = deskripsi
        self.__item = item
        self.__niceNpc = niceNpc
        self.__enemyNpc = enemyNpc

    # Setter dan Getter
    def set_nama(self, nama):
        self.__nama = nama

    def get_nama(self):
        return self.__nama
    
    def set_deskripsi(self, deskripsi):
        self.__deskripsi = deskripsi

    def get_deskripsi(self):
        return self.__deskripsi
    
    def set_item(self, item):
        self.__item = item

    def get_item(self):
        return self.__item

    def set_niceNpc(self, niceNpc):
        self.__niceNpc = niceNpc

    def get_niceNpc(self):
        return self.__niceNpc

    def set_enemyNpc(self, enemyNpc):
        self.__enemyNpc = enemyNpc

    def get_enemyNpc(self):
        return self.__enemyNpc