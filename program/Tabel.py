# Kelas Tabel
class Tabel:
    # Atribut
    __baris = 0
    __kolom = 0

    # Constructor
    def __init__(self, baris = "", kolom = ""):
        self.__baris = baris
        self.__kolom = kolom

    # Setter dan Getter
    def get_baris(self):
        return self.__baris
    
    def set_baris(self, baris):
        self.__baris = baris

    def get_kolom(self):
        return self.__kolom

    def set_kolom(self, kolom):
        self.__kolom = kolom

    # Method membuat tabel
    def buat_tabel(self, n_baris, n_kolom, isiTabel, headTabel):
        maxPerKolom = []  #Menampung max tiap kolom

        for index in range(n_kolom):
            maxPerKolom.append(0)

        # Mencari maxperkolom
        for kolom in range(n_kolom):
            maxPerKolom[kolom] = len(headTabel[kolom])
            for baris in range(n_baris):
                if(len(isiTabel[baris][kolom]) > maxPerKolom[kolom]):
                    maxPerKolom[kolom] = len(isiTabel[baris][kolom])
            maxPerKolom[kolom] += 1
        
        # buat garis pemisah baris
        self.pemisah_baris(n_kolom, maxPerKolom, '=')

        #Header tabel
        for kolom in range(n_kolom):
            print("| " + headTabel[kolom], end = "")
            if(len(headTabel[kolom]) < maxPerKolom[kolom]):
                for spasi in range(maxPerKolom[kolom]-len(headTabel[kolom])):
                    print(" ", end = "")
        print("|")

        # buat garis pemisah baris
        self.pemisah_baris(n_kolom, maxPerKolom, '=')

        #isi tabel
        for baris in range(n_baris):
            for kolom in range(n_kolom):
                print("| " + isiTabel[baris][kolom], end = "")

                if(len(headTabel[kolom]) < maxPerKolom[kolom]):
                    for spasi in range(maxPerKolom[kolom]-len(isiTabel[baris][kolom])):
                        print(" ", end = "")
            print("|")
            # buat garis pemisah baris
            self.pemisah_baris(n_kolom, maxPerKolom, '-')
                
    #Method membuat garis pemisah baris
    def pemisah_baris(self, n_kolom, maxPerKolom, simbol = ''):
        for kolom in range(n_kolom):
            for perkolom in range(maxPerKolom[kolom]):
                print(simbol, end='')
            print(simbol, end='')
            print(simbol, end='')
        print(simbol)
    


    def buat_tabel_notif(self, n_baris, isiTabel, warna):
        maxkolom = 0
        lenbaris = []
        
        for index in range(n_baris):
            lenbaris.append(0)
        # Mencari maxkolom
        for baris in range(n_baris):
            lenbaris[baris]  = len(isiTabel[baris])
            if(warna == 1):
                lenbaris[0] -= 9
                warna = 0
            if(lenbaris[baris] > maxkolom):
                maxkolom = lenbaris[baris]
        maxkolom += 2
        
        print("[", end="")
        for i in range(maxkolom):
            print("=", end="")
        print("]")

        for baris in range(n_baris):
            print("[ " + isiTabel[baris], end="")
            if(lenbaris[baris] < maxkolom):
                for i in range(maxkolom - lenbaris[baris]-1):
                    print(" ", end="")
            else:
                print(" ", end="")
            print("]")

        print("[", end="")
        for i in range(maxkolom):
            print("=", end="")
        print("]")

    def buat_tabel_status(self, isiTabel1, isiTabel2, head1, head2):
        # Cari maxlen
        maxlen = 29
        for dat in isiTabel1:
            if(len(dat)+15 > maxlen):
                maxlen = len(dat)+15

        # Garis atas
        for spasi in range(maxlen):
            print("=", end="")
        print("")

        # Tampilkan data karakter
        for i in range(4):
            print("| " + head1[i], end="")
            for j in range(9-len(head1[i])):
                print(" ", end="")
            print(": " + isiTabel1[i], end="")
            for spasi in range(maxlen-len(isiTabel1[i])-14):
                print(" ", end="")
            print("|")

        # Batas atas
        print("|      ", end="")
        for spasi in range(maxlen-8):
            print("-", end="")
        print("|")
        
        # Tampilkan status karakter
        for i in range(len(isiTabel2)):
            print("|      | "+ head2[i], end="")
            for j in range(12-len(head2[i])):
                print(" ", end="")
            print(": " + str(isiTabel2[i]), end="")
            if (i == 4):
                for spasi in range(maxlen-len(str(isiTabel2[i]))-15):
                    print(" ", end="")
                print("|")
            else:
                for spasi in range(maxlen-len(str(isiTabel2[i]))-24):
                    print(" ", end="")
                print("|")

        # Batas bawah
        print("|      ", end="")
        for spasi in range(maxlen-8):
            print("-", end="")
        print("|")

        # Tampilkan skill dan senjata
        for i in range(4, len(isiTabel1)):
            print("| " + head1[i], end="")
            for j in range(9-len(head1[i])):
                print(" ", end="")
            print(": " + isiTabel1[i], end="")
            for spasi in range(maxlen-len(isiTabel1[i])-14):
                print(" ", end="")
            print("|")

        # Garis bawah
        for spasi in range(maxlen):
            print("=", end="")
        print("")