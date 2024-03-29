from PlayerKarakter import PlayerKarakter

# Kelas Player
class Player:
    def __init__(self, idPlayer="", namaPlayer="", umur=0, playerkarakter=[]):
        self.__idPlayer = idPlayer
        self.__namaPlayer = namaPlayer
        self.__umur = umur
        self.__playerkarakter = playerkarakter  #Player memiliki karakter

    # Setter untuk idPlayer
    def set_idPlayer(self, idPlayer):
        self.__idPlayer = idPlayer

    # Getter untuk idPlayer
    def get_idPlayer(self):
        return self.__idPlayer

    # Setter untuk namaPlayer
    def set_namaPlayer(self, namaPlayer):
        self.__namaPlayer = namaPlayer

    # Getter untuk namaPlayer
    def get_namaPlayer(self):
        return self.__namaPlayer

    # Setter untuk umur
    def set_umur(self, umur):
        self.__umur = umur

    # Getter untuk umur
    def get_umur(self):
        return self.__umur
    
    # Setter untuk playerkarakter
    def set_playerkarakter(self, playerkarakter):
        self.__playerkarakter = playerkarakter

    # Getter untuk playerkarakter
    def get_playerkarakter(self):
        return self.__playerkarakter

    # Method untuk Menambah playerkarakter
    def tambah_playerkarakter(self, playerkarakter):
        self.__playerkarakter.append(playerkarakter)