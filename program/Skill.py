# Kelas Skill
class Skill:
    def __init__(self, id, nama="", efek=0, deskripsiEfek="", cooldown=0):
        self.__id = id
        self.__nama = nama
        self.__efek = efek                      #Jumlah efek yang diberikan
        self.__deskripsiEfek = deskripsiEfek
        self.__cooldown = cooldown              #Skill hanya dapat dilakukan setiap berapa detik sekali

    # Setter
    def set_id(self, id):
        self.__id = id

    def set_nama(self, nama):
        self.__nama = nama
    
    def set_efek(self, efek):
        self.__efek = efek

    def set_deskripsiEfek(self, deskripsiEfek):
        self.__deskripsiEfek = deskripsiEfek
    
    def set_cooldown(self, cooldown):
        self.__cooldown = cooldown

    # Getter
    def get_id(self):
        return self.__id
    
    def get_nama(self):
        return self.__nama

    def get_efek(self):
        return self.__efek

    def get_deskripsiEfek(self):
        return self.__deskripsiEfek
    
    def get_cooldown(self):
        return self.__cooldown
