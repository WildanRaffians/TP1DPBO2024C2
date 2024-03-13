class Skill:
    __nama = ""
    __efek = 0
    __deskripsiEfek = ""
    __cooldown = 0

    def __init__(self, nama="", efek=0, deskripsiEfek="", cooldown=0):
        self.__nama = nama
        self.__efek = efek
        self.__deskripsiEfek = deskripsiEfek
        self.__cooldown = cooldown

    # Setter
    def set_nama(self, nama):
        self.__nama = nama
    
    def set_efek(self, efek):
        self.__efek = efek

    def set_deskripsiEfek(self, deskripsiEfek):
        self.__deskripsiEfek = deskripsiEfek
    
    def set_cooldown(self, cooldown):
        self.__cooldown = cooldown

    # Getter
    def get_nama(self):
        return self.__nama

    def get_efek(self):
        return self.__efek

    def get_deskripsiEfek(self):
        return self.__deskripsiEfek
    
    def get_cooldown(self):
        return self.__cooldown
