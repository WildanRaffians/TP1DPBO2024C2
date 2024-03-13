#Class Item
class Item:
    def __init__(self, idItem="", nama="", deskripsi="", jumlah=0):
        self.__idItem = idItem
        self.__nama = nama
        self.__deskripsi = deskripsi
        self.__jumlah = jumlah

    # Setter
    def set_idItem(self, idItem):
        self.__idItem = idItem

    def set_nama(self, nama):
        self.__nama = nama

    def set_deskripsi(self, deskripsi):
        self.__deskripsi = deskripsi

    def set_jumlah(self, jumlah):
        self.__jumlah = jumlah

    # Getter
    def get_idItem(self):
        return self.__idItem

    def get_nama(self):
        return self.__nama

    def get_deskripsi(self):
        return self.__deskripsi

    def get_jumlah(self):
        return self.__jumlah
    
    
    