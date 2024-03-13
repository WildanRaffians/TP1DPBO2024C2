from Item import Item
import time

class Misi:
    __nama = ""
    __deskripsi = ""
    __hadiah = []
    __status = 0

    def __init__(self, nama, deskripsi, hadiah=[]):
        self.__nama = nama
        self.__deskripsi = deskripsi
        self.__hadiah = hadiah  # Inisialisasi daftar hadiah
        status = 0

    # Getter dan setter untuk atribut nama
    def set_nama(self, nama):
        self.__nama = nama

    def get_nama(self):
        return self.__nama

    # Getter dan setter untuk atribut deskripsi
    def set_deskripsi(self, deskripsi):
        self.__deskripsi = deskripsi

    def get_deskripsi(self):
        return self.__deskripsi

    # Getter dan setter untuk atribut hadiah
    def set_hadiah(self, hadiah):
        self.__hadiah = hadiah

    def get_hadiah(self):
        return self.__hadiah
    
    # Getter dan setter untuk atribut status
    def set_status(self, status):
        self.__status = status

    def get_status(self):
        return self.__status
    
    def melakukan_misi(self):
        time.sleep(1)
        print("Ayo " + self.get_deskripsi() + "!")
        time.sleep(1)
        print("Melakukan misi...")
        time.sleep(3)
        print("Berhasil!")

