class Npc:
    __nama = ""
    __job = ""

    def __init__(self, nama, job):
        self.__nama = nama
        self.__job = job

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
    