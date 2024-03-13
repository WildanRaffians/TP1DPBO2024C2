# from ItemDijual import ItemDijual
from Npc import Npc

# Kelas NPC baik, dapat memberi misi dan atau menjual item
class NiceNPC(Npc):
    def __init__(self, nama="", job="", itemDijual = [], misi = []):
        super().__init__(nama, job)
        self.__itemDijual = itemDijual
        self.__misi = misi

    # Setter dan getter
    def set_item_dijual(self, item):
        self.__itemDijual = item

    def get_item_dijual(self):
        return self.__itemDijual

    def set_misi(self, misi):
        self.__misi = misi

    def get_misi(self):
        return self.__misi