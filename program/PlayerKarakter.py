from Status import Status
from Senjata import Senjata
import time

class PlayerKarakter:
    def __init__(self, nama="", gender='', role="", status = "", senjata="", skill="", item=[]):
        self.__nama = nama
        self.__gender = gender
        self.__role = role
        self.__status = status
        self.__skill = skill
        self.__senjata = senjata
        self.__item = item

    # Getter dan setter untuk setiap atribut
    def set_nama(self, nama):
        self.__nama = nama

    def get_nama(self):
        return self.__nama

    def set_gender(self, gender):
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_role(self, role):
        self.__role = role

    def get_role(self):
        return self.__role

    def set_status(self, status):
        self.__status = status

    def get_status(self):
        return self.__status
    
    def set_senjata(self, senjata):
        self.__senjata = senjata

    def get_senjata(self):
        return self.__senjata

    def set_skill(self, skill):
        self.__skill = skill

    def get_skill(self):
        return self.__skill
    
    def set_item(self, item):
        self.__item = item

    def get_item(self):
        return self.__item
    
    def tambah_item(self, listItem):
        if isinstance(listItem, list):
            for it in listItem:
                for myit in self.__item:
                    if(myit.get_nama() == it.get_nama()):
                        temp = myit.get_jumlah()
                        myit.set_jumlah(temp + it.get_jumlah())
                        break
                else:
                    self.__item.append(it)
        else:
            for myit in self.__item:
                if(myit.get_nama() == listItem.get_nama()):
                    temp = myit.get_jumlah()
                    myit.set_jumlah(temp + 1)
                    break
            else:
                self.__item.append(listItem)

    def melawan_musuh(self):
        time.sleep(1)
        print("Tidak akan kubiarkan!")
        time.sleep(1)
        print("Melawan musuh...")
        time.sleep(3)

    def gunakan_skill(self):
        time.sleep(1)
        print("Rasakan Ini!")
        time.sleep(0.5)
        print("Skill " + self.get_skill().get_nama())