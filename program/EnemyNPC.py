from Npc import Npc
from Status import Status
from Skill import Skill
import time

# Kelas untuk NPC yang bisa dilawan / musuh
class EnemyNPC(Npc):
    def __init__(self, nama="", job="", status="", skill="", dropItem=[]):
        super().__init__(nama, job)
        self.__status = status
        self.__skill = skill
        self.__dropItem = dropItem
        self.__statHidup = True

    # Setter dan getter setiap atribut
    def set_status(self, status):
        self.__status = status

    def get_status(self):
        return self.__status

    def set_skill(self, skill):
        self.__skill = skill

    def get_skill(self):
        return self.__skill

    def set_drop_item(self, dropItem):
        self.__dropItem = dropItem

    def get_drop_item(self):
        return self.__dropItem
    
    def set_statHidup(self, statHidup):
        self.__statHidup = statHidup

    def get_statHidup(self):
        return self.__statHidup
    
    # Method musuh menggertak
    def menggertak(self):
        time.sleep(1)
        print("(Aku " + self.get_nama() + ", Akan kuhacurkan kau!)")

    # Method musuh terkena serangan
    def terkena_serangan(self):
        time.sleep(1)
        print("(ugh...)")
        time.sleep(1)
        print("(Tidak Mungkin...)")
        time.sleep(1)

    # Method Musuh menggunakan skill
    def gunakan_skill(self):
        time.sleep(1)
        print("(Rasakanlah!)")
        time.sleep(0.5)
        print("(Skill, " + self.get_skill().get_nama() + "!)")