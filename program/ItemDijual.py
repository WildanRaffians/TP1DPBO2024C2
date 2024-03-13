from Item import Item

class ItemDijual(Item):
    __harga = 0
    __status = 0

    from Item import Item

    def __init__(self, idItem="", nama="", deskripsi="", jumlah=0, harga=0):
        super().__init__(idItem, nama, deskripsi, jumlah)
        self.__harga = harga
        self.__status = 0

    def set_harga(self, harga):
        self.__harga = harga

    def get_harga(self):
        return self.__harga
    
    def set_status(self, status):
        self.__status = status

    def get_status(self):
        return self.__status
