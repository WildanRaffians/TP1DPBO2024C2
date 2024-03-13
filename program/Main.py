# Saya Wildan Hafizh Raffianshar NIM [2202301] mengerjakan soal Tugas Praktikum-1
# dalam mata kuliah DPBO untuk keberkahanNya maka saya tidak melakukan kecurangan 
# seperti yang telah dispesifikasikan. Aamiin

#Kelas Main

#siapkan kelas yang dibutuhkan
from Skill import Skill
from Senjata import Senjata
from Status import Status
from Player import Player
from PlayerKarakter import PlayerKarakter
from Misi import Misi
from NiceNPC import NiceNPC
from EnemyNPC import EnemyNPC
from Item import Item
from ItemDijual import ItemDijual
from Wilayah import Wilayah
from Tabel import Tabel
from colorama import init, Fore, Back, Style
import time

# Inisialisasi colorama
init()

# Siapkan data------------------------\
# Data status
statusDPS = Status(1, 1000, 100, 500, 800)
statusSupport = Status(1, 1000, 100, 200, 1000)
statusHealer = Status(1, 1800, 100, 100, 600)
statusEnemy1 = Status(5, 1500, 100, 800, 1000)

# Data senjata
listSenjata = []
listSenjata.append(Senjata("Pedang", "Dull Blade", 560, "ATK", 35))
listSenjata.append(Senjata("Panah", "Aqua Simularca", 580, "DEF", 35))
listSenjata.append(Senjata("Tombak", "Engulfing Lightning", 580, "ATK", 45))
listSenjata.append(Senjata("Tongkat Sihir", "Everlasting Moonglow", 580, "Max HP", 55))

# Data Skill
listSkillDPS = []
listSkillHealer = []
listSkillSupport = []
terjanganEs = Skill("Terjangan ES", 240, "Menerbangkan bunga es ke arah musuh, Mengakibatkan DMG sebesar 240% ATK", 10)
bolaApi = Skill("Bola Api", 240, "Menembakkan bola api ke arah musuh, Mengakibatkan DMG sebesar 240% ATK", 10)
listSkillDPS.append(terjanganEs)
listSkillDPS.append(bolaApi)
listSkillHealer.append(Skill("Kelopak Bunga", 20, "Mengeluarkan kelopak bunga raksasa, Memulihkan HP pemilik skill dan rekan tim sebesar 20% Max HP", 15))
listSkillSupport.append(Skill("Penempa Baja", 12, "Mengeluarkan Palu penempa, Meningkatkan ATK rekan tim sebesar 12% ATK pengguna", 20))

# Data Item
item01 = Item("IT0001", "Koin", "Mata uang untuk jual beli", 100000)
item21 = Item("IT0021", "Koin", "Mata uang untuk jual beli", 50000)
item22 = Item("IT0022", "Batu Ajaib", "Batu memancarkan cahaya yang aneh tapi menyejukan, pasti berguna suatu saat", 1)
item23 = Item("IT0021", "Koin", "Mata uang untuk jual beli", 20000)
item24 = Item("IT0024", "Bola Salju", "Bola salju sekepal tangan", 4)
item31 = Item("IT0031", "Dandelion", "Bunga Dandelion", 5)
item32 = Item("IT0032", "Cecilia", "Bunga Cecilia", 5)
item33 = Item("IT0033", "Burnett", "Bunga Burnett", 5)
item34 = Item("IT0034", "Hybrid Prikly Burr", "Bunga Hybrid Prikly Burr", 5)

# Data item dijual
itemj11 = ItemDijual("ITJ0011", "Ramuan Rahasia", "Ramuan yang memeberikan efek tertentu", 10, 2000)
itemj12 = ItemDijual("ITJ0012", "Ramuan Rahasia2", "Ramuan yang memeberikan efek tertentu", 10, 2000)

listItemku = []
listItemku.append(item01)
listItemKhatarine = []
listItemKhatarine.append(itemj11)
listItemKhatarine.append(itemj12)

# Data misi dan hadiah
misiKatarine = []
listHadiahK1 = []
listHadiahK2 = []
listHadiahK1.append(item21)
listHadiahK1.append(item22)
listHadiahK2.append(item23)
misi1 = Misi("Sang Putri Berkelana", "Mengawal Putri dari Kerajaan Belobog ke kerajaan Penacony", listHadiahK1)
misi2 = Misi("Bandit Jembatan Meresahkan", "Kalahkan bandit yang ada di jembatan", listHadiahK2)

listMisiK = []
listMisiK.append(misi1)
listMisiK.append(misi2)
Khatarine1 = NiceNPC("Khatarine", "Resepsionis Guild", listItemKhatarine, listMisiK)

# Data item dan NPC di wilayah
listItemMondo = []
listItemMondo.append(item31)
listItemMondo.append(item32)
listItemBolobog = []
listItemBolobog.append(item33)
listItemBolobog.append(item34)
listNiceNPCMondo = []
listNiceNPCMondo.append(Khatarine1)

# Data enemy
dropItemEnemy1 = []
dropItemEnemy1.append(item23)
dropItemEnemy1.append(item24)
enemyBolobog1 = EnemyNPC("Gordon", "Penjaga Gua", statusEnemy1, terjanganEs, dropItemEnemy1)
listEnemyNPCBolobog = []
listEnemyNPCBolobog.append(enemyBolobog1)

# Wilayah
mondo = Wilayah("Mondo", "Ini Merupakan kota awal bagi para petualang pemula.", listItemMondo, listNiceNPCMondo)
bolobog = Wilayah("Bolobog", "Kota yang sudah diselimuti es selama ratusan tahun", listItemBolobog, enemyNpc=listEnemyNPCBolobog)

listWilayah = []
listWilayah.append(mondo)
listWilayah.append(bolobog)

# Tampilan =================================================================================================================
# Masukkan nama dan umur player
print("Isi Data...")
namaPlayer = str(input("Nama Player : "))
umurPlayer = int(input("Umur Player : "))
player1 = Player("P0001", namaPlayer, umurPlayer)

# Selamat Datang
print("")
notif = Tabel()
haiPlayer = "Hai " + Fore.BLUE + player1.get_namaPlayer() + Style.RESET_ALL + "!"
selamatDatang = "Selamat Datang di Game Odisea!"
isiNotif = [haiPlayer, selamatDatang]
notif.buat_tabel_notif(2, isiNotif, 1)
print("")

# Buat karakter
print("Berpetualang di dunia yang menakjubkan.")
print("")
print("Ayo Buat Karaktermu!")
time.sleep(0.5)
karakter1 = PlayerKarakter()
# Nama karakter
namaKar = str(input("Nama Karakter : "))
karakter1.set_nama(namaKar)
# Gender Karakter
gender = 0
while(gender == 0):
    print("")
    print("Gender Karakter :")
    print("1. Laki-Laki")
    print("2. Perempuan")
    print("")
    gender = int(input("> "))
    if(gender == 1):
        karakter1.set_gender('L')
    elif(gender == 2):
        karakter1.set_gender('P')
    else:
        print("")
        print("[[Pilihan Tidak Valid]]")
        print("")
        gender = 0

# Role Karakter
role = 0
while(role == 0):
    print("")
    print("Pilih Role : ")
    print("1. DPS")
    print("2. Support")
    print("3. Healer")
    print("")
    role = int(input("> "))
    print("")

# Pilih skill berdasar role 
    if(role == 1):
        # Role DPS
        karakter1.set_role("DPS")
        print("Silahkan Pilih Skill yang Kamu Inginkan :")
        #Tabel Skill
        isiTabel = [[0 for _ in range(5)] for _ in range(len(listSkillDPS))]
        i = 0
        for skill in listSkillDPS :
            isiTabel[i][0] = str(i+1)
            isiTabel[i][1] = skill.get_nama()
            isiTabel[i][2] = str(skill.get_efek())
            isiTabel[i][3] = skill.get_deskripsiEfek()
            isiTabel[i][4] = str(skill.get_cooldown())
            i+=1

        #siapkan header
        head = ["No", "Nama", "Efek (%)", "Deskripsi", "CD (s)"]
        
        #tampilkan tabel
        tab = Tabel()
        tab.buat_tabel(len(listSkillDPS), 5, isiTabel, head)

        skillfound = 0
        while(skillfound == 0):
            print("")
            skill = int(input("> "))

            for i in range(len(listSkillDPS)):
                if i == (skill-1):
                    karakter1.set_skill(listSkillDPS[i])
                    skillfound = 1
            if(skillfound == 0):
                print("")
                print("[[Pilihan Tidak Valid]]")
                print("")
            karakter1.set_status(statusDPS)

    elif(role == 2):
        karakter1.set_role("Support")
        print("Silahkan Pilih Skill yang Kamu Inginkan :")
        #Tabel Skill
        isiTabel = [[0 for _ in range(5)] for _ in range(len(listSkillSupport))]
        i = 0
        for skill in listSkillSupport :
            isiTabel[i][0] = str(i+1)
            isiTabel[i][1] = skill.get_nama()
            isiTabel[i][2] = str(skill.get_efek())
            isiTabel[i][3] = skill.get_deskripsiEfek()
            isiTabel[i][4] = str(skill.get_cooldown())
            i+=1

        #siapkan header
        head = ["No", "Nama", "Efek (%)", "Deskripsi", "CD (s)"]
        
        #tampilkan tabel
        tab = Tabel()
        tab.buat_tabel(len(listSkillSupport), 5, isiTabel, head)

        skillfound = 0
        while(skillfound == 0):
            print("")
            skill = int(input("> "))

            for i in range(len(listSkillSupport)):
                if i == (skill-1):
                    karakter1.set_skill(listSkillSupport[i])
                    skillfound = 1
            if(skillfound == 0):
                print("")
                print("[[Pilihan Tidak Valid]]")
                print("")
            karakter1.set_status(statusSupport)

    elif(role == 3):
        karakter1.set_role("Healer")
        print("Silahkan Pilih Skill yang Kamu Inginkan :")
        #Tabel Skill
        isiTabel = [[0 for _ in range(5)] for _ in range(len(listSkillHealer))]
        i = 0
        for skill in listSkillHealer :
            isiTabel[i][0] = str(i+1)
            isiTabel[i][1] = skill.get_nama()
            isiTabel[i][2] = str(skill.get_efek())
            isiTabel[i][3] = skill.get_deskripsiEfek()
            isiTabel[i][4] = str(skill.get_cooldown())
            i+=1

        #siapkan header
        head = ["No", "Nama", "Efek (%)", "Deskripsi", "CD (s)"]
        
        #tampilkan tabel
        tab = Tabel()
        tab.buat_tabel(len(listSkillHealer), 5, isiTabel, head)

        skillfound = 0
        while(skillfound == 0):
            print("")
            skill = int(input("> "))

            for i in range(len(listSkillSupport)):
                if i == (skill-1):
                    karakter1.set_skill(listSkillSupport[i])
                    skillfound = 1
            if(skillfound == 0):
                print("")
                print("[[Pilihan Tidak Valid]]")
                print("")
            karakter1.set_status(statusSupport)
    else:
        print("")
        print("[[Pilihan Tidak Valid]]")
        print("")
        role = 0
        
# Pilih Senjata awal
#Tabel Senjata
print("")
print("Silahkan Pilih Senjata Pertamamu!")
isiTabel = [[0 for _ in range(6)] for _ in range(len(listSenjata))]
i = 0
for senjata in listSenjata :
    isiTabel[i][0] = str(i+1)
    isiTabel[i][1] = senjata.get_tipe()
    isiTabel[i][2] = senjata.get_nama()
    isiTabel[i][3] = str(senjata.get_kenaikanAtk())
    isiTabel[i][4] = senjata.get_statBonus()
    isiTabel[i][5] = str(senjata.get_kenaikanStatBonus())
    i+=1

#siapkan header
head = ["No", "Tipe", "Nama", "+ ATK", "Bonus", "+ Bonus %"]

#tampilkan tabel
tab = Tabel()
tab.buat_tabel(len(listSenjata), 6, isiTabel, head)

# Add senjata pilihan
senjatafound = 0
while (senjatafound==0):
    print("")
    senjata = int(input("> "))

    for i in range(len(listSenjata)):
        if i == (senjata-1):
            karakter1.set_senjata(listSenjata[i])
            senjatafound = 1
    if(senjatafound == 0):
        print("")
        print("[[Pilihan Tidak Valid]]")
        print("")

# Set item awal
karakter1.set_item(listItemku)
time.sleep(1)
print("")

# Karakter berhasil dibuat
berhasil = "Karakter Berhasil dibuat!"
isiNotif = [berhasil]
notif.buat_tabel_notif(1, isiNotif, 0)

print("")

input("Tekan Enter...")
print("")

player1.tambah_playerkarakter(karakter1)

# Tampilkan status karakter
print("Status Karakter:")
isiTabel1 = []
isiTabel2 = []

isiTabel1.append(karakter1.get_nama())
isiTabel1.append(karakter1.get_gender())
isiTabel1.append(karakter1.get_role())
isiTabel1.append("")
isiTabel1.append(karakter1.get_skill().get_nama())
isiTabel1.append(karakter1.get_senjata().get_nama())
    
isiTabel2.append(str(karakter1.get_status().get_level()))
isiTabel2.append(str(karakter1.get_status().get_maxHP()))
isiTabel2.append(str(karakter1.get_status().get_atk()))
isiTabel2.append(str(karakter1.get_status().get_defense()))
isiTabel2.append(Fore.GREEN + str(karakter1.get_status().get_hp()) + "%" + Style.RESET_ALL)

head1 = ["Nama", "Gender", "Role", "Status", "Skill", "Senjata"]
head2 = ["Level", "Max HP", "ATK", "DEF", "HP Saat Ini"]

tab.buat_tabel_status(isiTabel1, isiTabel2, head1, head2)

# Tampilkan Item
#Tabel Item
print("")
print("Itemku")
isiTabel = [[0 for _ in range(4)] for _ in range(len(listItemku))]
i = 0
for item in listItemku :
    isiTabel[i][0] = str(i+1)
    isiTabel[i][1] = item.get_nama()
    isiTabel[i][2] = item.get_deskripsi()
    isiTabel[i][3] = str(item.get_jumlah())
    i+=1

#siapkan header
head = ["No", "Nama", "Deskripsi", "Jumlah"]

#tampilkan tabel
tab = Tabel()
tab.buat_tabel(len(listItemku), 4, isiTabel, head)

# time.sleep(1)
print("")
print("")
berpetualang = "Waktunya Berpetualang!"
isiNotif = [berpetualang]
notif.buat_tabel_notif(1, isiNotif, 0)

print("")

input("Tekan Enter...")
print("")

wilayah = 0     #Wilayah awal
exit = 0    
aksi = -1       #input
while(aksi != exit):
    # Menu
    print("")
    print("")
    selamatDatang = "Selamat Datang di "+ Fore.CYAN + listWilayah[wilayah].get_nama() + Style.RESET_ALL + "!" 
    isiNotif = [selamatDatang]
    notif.buat_tabel_notif(1, isiNotif, 1)
    print("")
    print("[[ " + listWilayah[wilayah].get_deskripsi() + " ]]")
    print("")
    print("")
    print("Apa yang ingin kamu lakukan?")
    print("")
    print("1. Cari NPC")
    print("2. Cari Item")
    print("3. Cari Musuh")
    print("4. Lihat Status Karakterku")
    print("5. Lihat Itemku")
    print("6. Lihat Map")
    print("")
    print(Fore.RED + "0. Keluar Game" + Style.RESET_ALL)

    print("")
    aksi = int(input("> "))
    print("")
    
    if(aksi == 1):
        # Cari NPC
        aksi = -1
        end = 0

        while(end==0):
            if(len(listWilayah[wilayah].get_niceNpc()) == 0):
                print("[[Tidak ada NPC disini]]")
            else:
                #Tabel NPC
                isiTabel = [[0 for _ in range(2)] for _ in range(len(listWilayah[wilayah].get_niceNpc()))]
                i = 0
                for npc in listWilayah[wilayah].get_niceNpc() :
                    isiTabel[i][0] = str(i+1)
                    isiTabel[i][1] = npc.get_nama()
                    i+=1

                #siapkan header
                print("NPC yang ada di " + listWilayah[wilayah].get_nama())
                head = ["No", "Nama"]

                #tampilkan tabel
                tab = Tabel()
                tab.buat_tabel(len(listWilayah[wilayah].get_niceNpc()), 2, isiTabel, head)

            print("")
            i = 1
            for npc in range(len(listWilayah[wilayah].get_niceNpc())):
                print(str(npc+1) + ". " + "Interaksi NPC " + str(npc+1))
                i+=1
            
            print(str(i) + ". " + "Kembali")

            print("")
            aksi = int(input("> "))
            print("")

            if(aksi != i):
                # NPC terpilih
                npc = aksi-1
                print("(Hai! Saya " + listWilayah[wilayah].get_niceNpc()[npc].get_nama() + ", ada yang bisa saya bantu?)")

                print("")
                nom = 1
                print("1. Ada misi yang bisa aku kerjakan hari ini?")
                print("2. Item apa saja yang kamu jual?")
                print("3. Sampai jumpa")

                print("")
                aksi = int(input("> "))
                print("")

                if(aksi == 1):
                    # Misi
                    statmisi1 = 0
                    statmisi0 = 0
                    for misi in listWilayah[wilayah].get_niceNpc()[npc].get_misi() :
                        if(misi.get_status() == 1):
                            statmisi1 += 1
                        else:
                            statmisi0 += 1
                    n_misi = len(listWilayah[wilayah].get_niceNpc()[npc].get_misi())

                    if(statmisi1 == n_misi or n_misi == 0):
                        print("(Tidak ada misi untuk hari ini)")
                        print("")
                        time.sleep(1)
                    else:
                        isiTabel = [[0 for _ in range(3)] for _ in range(statmisi0)]
                        i = 0
                        idxAwal = 0
                        for misi in listWilayah[wilayah].get_niceNpc()[npc].get_misi() :
                            if(misi.get_status() == 0):
                                isiTabel[i][0] = str(idxAwal+1)
                                isiTabel[i][1] = misi.get_nama()
                                isiTabel[i][2] = misi.get_deskripsi()
                                i+=1
                            idxAwal+=1

                        #siapkan header
                        print("Tentu! Silahkan pilih salah satu:")
                        head = ["No", "Judul", "Deskripsi"]
                        
                        tab = Tabel()
                        tab.buat_tabel(statmisi0, 3, isiTabel, head)

                        print("")
                        aksi = int(input("> "))
                        print("")
                        # print(aksi)
                        time.sleep(1)

                        if(1 <= aksi <= idxAwal):
                            misi = aksi-1
                            if(listWilayah[wilayah].get_niceNpc()[npc].get_misi()[misi].get_status() == 1):
                                print("")
                                print("[[Masukan tidak valid]]")
                                print("")
                            else:
                                listWilayah[wilayah].get_niceNpc()[npc].get_misi()[misi].sedang_dikerjakan()
                                # print(misi)
                                
                                print("")
                                selamat = Fore.CYAN + "Selamat!" + Style.RESET_ALL
                                misif = listWilayah[wilayah].get_niceNpc()[npc].get_misi()[misi].get_nama() + " Telah Selesai!"
                                isiNotif = [selamat, misif]
                                notif.buat_tabel_notif(2, isiNotif, 1)
                                print("")

                                listWilayah[wilayah].get_niceNpc()[npc].get_misi()[misi].set_status(1)

                                time.sleep(0.5)
                                print("Hadiahmu:")
                                
                                isiTabel = [[0 for _ in range(4)] for _ in range(len(listWilayah[wilayah].get_niceNpc()[npc].get_misi()[misi].get_hadiah()))]
                                i = 0
                                for hadiah in listWilayah[wilayah].get_niceNpc()[npc].get_misi()[misi].get_hadiah() :
                                    isiTabel[i][0] = str(i+1)
                                    isiTabel[i][1] = hadiah.get_nama()
                                    isiTabel[i][2] = hadiah.get_deskripsi()
                                    isiTabel[i][3] = str(hadiah.get_jumlah())
                                    i+=1

                                #siapkan header
                                head = ["No", "Nama", "Deskripsi", "Jumlah"]
                                
                                tab = Tabel()
                                tab.buat_tabel(len(listWilayah[wilayah].get_niceNpc()[npc].get_misi()[misi].get_hadiah()), 4, isiTabel, head)

                                karakter1.tambah_item(listWilayah[wilayah].get_niceNpc()[npc].get_misi()[misi].get_hadiah())

                            print("")
                            input("Tekan Enter...")
                            print("")
                elif(aksi == 2):
                    # Beli item
                    endbeli = 0
                    aksi = -1
                    while(endbeli==0):
                        statitem1 = 0
                        statitem0 = 0
                        for item in listWilayah[wilayah].get_niceNpc()[npc].get_item_dijual() :
                            if(item.get_status() == 1):
                                statitem1 += 1
                            else:
                                statitem0 += 1
                        time.sleep(0.5)
                        n_item = len(listWilayah[wilayah].get_niceNpc()[npc].get_item_dijual())
                        if(statitem1 == n_item or n_item == 0):
                            print("(maaf, aku tidak sedang menjual apa-apa saat ini)")
                            print("")
                            time.sleep(1)
                        else:
                            print("Oh, Aku menjual...")
                            isiTabel = [[0 for _ in range(5)] for _ in range(statitem0)]
                            i = 0
                            idxAwal = 0
                            for item_dijual in listWilayah[wilayah].get_niceNpc()[npc].get_item_dijual() :
                                
                                if(item_dijual.get_status() == 0):
                                    isiTabel[i][0] = str(idxAwal+1)
                                    isiTabel[i][1] = item_dijual.get_nama()
                                    isiTabel[i][2] = item_dijual.get_deskripsi()
                                    isiTabel[i][3] = str(item_dijual.get_harga())
                                    isiTabel[i][4] = str(item_dijual.get_jumlah())
                                    i+=1
                                idxAwal += 1

                            #siapkan header
                            head = ["No", "Nama", "Deskripsi", "Harga", "Jumlah"]
                            
                            tab = Tabel()
                            tab.buat_tabel(statitem0, 5, isiTabel, head)

                            print("")
                            print("Ada yang mau kamu beli?")
                            print("")
                            print("[Pilih Nomor item jika ingin membeli.]")
                            print(str(idxAwal+1) + ". Tidak terima kasih")
                            print("")
                            aksi = int(input("> "))
                            print("")

                            time.sleep(0.5)
                            if(1 <= aksi <= idxAwal):
                                beli = aksi-1
                                if(listWilayah[wilayah].get_niceNpc()[npc].get_item_dijual()[beli].get_status() == 1):
                                    print("")
                                    print("[[Masukan tidak valid]]")
                                    print("")
                                else:
                                    temp = listWilayah[wilayah].get_niceNpc()[npc].get_item_dijual()[beli].get_jumlah()
                                    listWilayah[wilayah].get_niceNpc()[npc].get_item_dijual()[beli].set_jumlah(temp-1)
                                    item_dibeli = Item()
                                    item_dibeli.set_idItem(listWilayah[wilayah].get_niceNpc()[npc].get_item_dijual()[beli].get_idItem())
                                    item_dibeli.set_nama(listWilayah[wilayah].get_niceNpc()[npc].get_item_dijual()[beli].get_nama())
                                    item_dibeli.set_deskripsi(listWilayah[wilayah].get_niceNpc()[npc].get_item_dijual()[beli].get_deskripsi())
                                    item_dibeli.set_jumlah(1)
                                    karakter1.tambah_item(item_dibeli)
                                    
                                    print("")
                                    selamatitem = "1 item telah dibeli!"
                                    namaitem = listWilayah[wilayah].get_niceNpc()[npc].get_item_dijual()[beli].get_nama()
                                    isiNotif = [selamatitem, namaitem]
                                    notif.buat_tabel_notif(2, isiNotif, 0)
                                    print("")

                                    if(listWilayah[wilayah].get_niceNpc()[npc].get_item_dijual()[beli].get_jumlah() == 0):
                                        listWilayah[wilayah].get_niceNpc()[npc].get_item_dijual()[beli].set_status(1)

                                input("Tekan Enter...")
                                print("")
                                time.sleep(1)
                            elif(aksi == idxAwal+1):
                                print("(Baiklah...)")
                                print("")
                                endbeli=1
                elif(aksi == 3):
                    print("")
                    print("(Sampai Ketemu di lain waktu...)")
                    print("")
                    input("Tekan Enter...")
                    print("")
            elif(aksi == i):
                end=1
                
    elif(aksi == 2):
        # Cari item di wilayah
        aksi = -1
        i = -1
        while(aksi != i+1):
            if(len(listWilayah[wilayah].get_item()) == 0):
                print("[[Tidak ada item disini]]")
            else:
                #Tabel Item
                isiTabel = [[0 for _ in range(4)] for _ in range(len(listWilayah[wilayah].get_item()))]
                i = 0
                for item in listWilayah[wilayah].get_item() :
                    isiTabel[i][0] = str(i+1)
                    isiTabel[i][1] = item.get_nama()
                    isiTabel[i][2] = item.get_deskripsi()
                    isiTabel[i][3] = str(item.get_jumlah())
                    i+=1

                #siapkan header
                print("Item yang ada di " + listWilayah[wilayah].get_nama())
                head = ["No", "Nama", "Deskripsi", "Jumlah"]

                #tampilkan tabel
                tab = Tabel()
                tab.buat_tabel(len(listWilayah[wilayah].get_item()), 4, isiTabel, head)

            print("")
            print("[Pilih Nomor item jika ingin mengambil.]")
            print(str(i+1) + ". Kembali")
            print("")
            aksi = int(input("> "))
            print("")
            time.sleep(1)
            if(aksi != i+1):
                item = aksi-1
                if(listWilayah[wilayah].get_item()[item].get_jumlah() <= 0):
                    print("") 
                    print("[[Jumlah Item 0! Silahkan pilih item lain]]") 
                    print("") 
                else:
                    temp = listWilayah[wilayah].get_item()[item].get_jumlah()
                    listWilayah[wilayah].get_item()[item].set_jumlah(temp-1)
                    item_didapat = Item()
                    item_didapat.set_idItem(listWilayah[wilayah].get_item()[item].get_idItem())
                    item_didapat.set_nama(listWilayah[wilayah].get_item()[item].get_nama())
                    item_didapat.set_deskripsi(listWilayah[wilayah].get_item()[item].get_deskripsi())
                    item_didapat.set_jumlah(1)
                    karakter1.tambah_item(item_didapat)

                    print("")
                    selamatitem = "1 item berhasil didapat!"
                    namaitem = listWilayah[wilayah].get_item()[item].get_nama()
                    isiNotif = [selamatitem, namaitem]
                    notif.buat_tabel_notif(2, isiNotif, 0)
                    print("")

                input("Tekan Enter...")
                print("")
                
    elif(aksi == 3):
        # Cari musuh di wilayah
        aksi = -1
        end = 0

        while(end==0):
            #Tabel NPC
            statmusuh1 = 0
            statmusuh0 = 0
            for musuh in listWilayah[wilayah].get_enemyNpc() :
                if(musuh.get_statHidup() == True):
                    statmusuh1 += 1
                else:
                    statmusuh0 += 1
            n_musuh = len(listWilayah[wilayah].get_enemyNpc())
            
            if(statmusuh0 == n_musuh or n_musuh == 0):
                print("")
                print("[[Tidak ada musuh disini]]")
                print("")
                time.sleep(1)
                end = 1
            else:
                print("Musuh yang ada di " + listWilayah[wilayah].get_nama())
                isiTabel = [[0 for _ in range(2)] for _ in range(statmusuh1)]
                i = 0
                idxAwal = 0
                for npc in listWilayah[wilayah].get_enemyNpc() :
                    if(npc.get_statHidup() == True):
                        isiTabel[i][0] = str(idxAwal+1)
                        isiTabel[i][1] = npc.get_nama()
                        i+=1
                    idxAwal +=1

                head = ["No", "Nama"]

                #tampilkan tabel
                tab = Tabel()
                tab.buat_tabel(statmusuh1, 2, isiTabel, head)

                print("")
                print("[[Pilih nomor musuh untuk melawannya!]]")
                print("")
                
                print(str(idxAwal+1) + ". " + "Kembali")

                print("")
                aksi = int(input("> "))
                print("")

                if(aksi != idxAwal+1):
                    npc = aksi-1
                    if(listWilayah[wilayah].get_enemyNpc()[npc].get_statHidup() == False):
                        print("")
                        print("[[Perintah tidak valid]]")
                        print("")
                    else:
                        listWilayah[wilayah].get_enemyNpc()[npc].menggertak()
                        karakter1.melawan_musuh()
                        karakter1.gunakan_skill()
                        listWilayah[wilayah].get_enemyNpc()[npc].terkena_serangan()

                        print("")
                        selamat = Fore.CYAN + "Selamat!" + Style.RESET_ALL
                        enemyf = listWilayah[wilayah].get_enemyNpc()[npc].get_nama() + " Telah Dikalahkan!"
                        isiNotif = [selamat, enemyf]
                        notif.buat_tabel_notif(2, isiNotif, 1)
                        print("")
                        time.sleep(0.5)

                        listWilayah[wilayah].get_enemyNpc()[npc].set_statHidup(False)
                        
                        print("Drop item yang didapat:")
                        isiTabel = [[0 for _ in range(4)] for _ in range(len(listWilayah[wilayah].get_enemyNpc()[npc].get_drop_item()))]
                        i = 0
                        for hadiah in listWilayah[wilayah].get_enemyNpc()[npc].get_drop_item() :
                            isiTabel[i][0] = str(i+1)
                            isiTabel[i][1] = hadiah.get_nama()
                            isiTabel[i][2] = hadiah.get_deskripsi()
                            isiTabel[i][3] = str(hadiah.get_jumlah())
                            i+=1

                        #siapkan header
                        head = ["No", "Nama", "Deskripsi", "Jumlah"]
                        
                        tab = Tabel()
                        tab.buat_tabel(len(listWilayah[wilayah].get_enemyNpc()[npc].get_drop_item()), 4, isiTabel, head)
                        
                        karakter1.tambah_item(listWilayah[wilayah].get_enemyNpc()[npc].get_drop_item())

                    print("")
                    input("Tekan Enter...")
                elif(aksi == idxAwal+1):
                    end=1
    elif(aksi == 4):
        # Tampilkan status karakter
        print("Status Karakter:")
        isiTabel1 = []
        isiTabel2 = []

        isiTabel1.append(karakter1.get_nama())
        isiTabel1.append(karakter1.get_gender())
        isiTabel1.append(karakter1.get_role())
        isiTabel1.append("")
        isiTabel1.append(karakter1.get_skill().get_nama())
        isiTabel1.append(karakter1.get_senjata().get_nama())
            
        isiTabel2.append(str(karakter1.get_status().get_level()))
        isiTabel2.append(str(karakter1.get_status().get_maxHP()))
        isiTabel2.append(str(karakter1.get_status().get_atk()))
        isiTabel2.append(str(karakter1.get_status().get_defense()))
        isiTabel2.append(Fore.GREEN + str(karakter1.get_status().get_hp()) + "%" + Style.RESET_ALL)

        head1 = ["Nama", "Gender", "Role", "Status", "Skill", "Senjata"]
        head2 = ["Level", "Max HP", "ATK", "DEF", "HP Saat Ini"]

        tab.buat_tabel_status(isiTabel1, isiTabel2, head1, head2)

        print("")
        input("Tekan Enter...")
        print("")
    
    elif(aksi == 5):
        # Tampilkan Item
        #Tabel Item
        print("")
        print("Itemku")
        isiTabel = [[0 for _ in range(4)] for _ in range(len(karakter1.get_item()))]
        i = 0
        for item in karakter1.get_item() :
            isiTabel[i][0] = str(i+1)
            isiTabel[i][1] = item.get_nama()
            isiTabel[i][2] = item.get_deskripsi()
            isiTabel[i][3] = str(item.get_jumlah())
            i+=1

        #siapkan header
        head = ["No", "Nama", "Deskripsi", "Jumlah"]

        #tampilkan tabel
        tab = Tabel()
        tab.buat_tabel(len(karakter1.get_item()), 4, isiTabel, head)
        
        print("")
        input("Tekan Enter...")
        print("")
    elif(aksi == 6):
        # Tampilkan WIlayah
        #Tabel Wilayah
        print("")
        print("Wilayah Pulau Ini")
        isiTabel = [[0 for _ in range(2)] for _ in range(len(listWilayah))]
        i = 0
        for item in listWilayah :
            isiTabel[i][0] = str(i+1)
            isiTabel[i][1] = item.get_nama()
            i+=1

        #siapkan header
        head = ["No", "Nama"]

        #tampilkan tabel
        tab = Tabel()
        tab.buat_tabel(len(listWilayah), 2, isiTabel, head)
        
        print("")
        print("Pergi ke...")
        print("[[Pilih nomor wilayah untuk pergi]]")
        print("")
        aksi = int(input("> "))
        print("")

        wilayah = aksi-1    #Ganti wilayah
        print("")
        print("[[Menuju " + listWilayah[wilayah].get_nama() + "...]]")
        print("")
        time.sleep(1)
    elif(aksi == 0):
        print("")
        print("[[Yakin keluar dari game?]]")
        print("")
        print("1. Ya")
        print("2. Tidak")
        print("")

        aksi = int(input("> "))

        if(aksi == 2):
            aksi = -1
        elif(aksi == 1):
            aksi = 0
            print("")
            print("[[Kamu akan keluar dari game...]]")
            time.sleep(2)
            print("")
            isiNotif = ["Terima kasih telah berpetualang!"]
            notif.buat_tabel_notif(1, isiNotif, 0)
            print("")
    else:
        print("")
        print("Pilihan Tidak Valid")
        print("")
        