# Kelas NPC
class Npc:
    def __init__(self, id="", nama="", job=""):
        self.__id = id
        self.__nama = nama
        self.__job = job

    # Getter dan setter untuk atribut id
    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id
    
    # Getter dan setter untuk atribut nama
    def set_nama(self, nama):
        self.__nama = nama

    def get_nama(self):
        return self.__nama

    # Getter dan setter untuk atribut job
    def set_job(self, job):
        self.__job = job

    def get_job(self):
        return self.__job
    