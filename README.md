<h1>TP1DPBO2024C2</h1>
<h3>Janji</h3>
Saya Wildan Hafizh Raffianshar NIM [2202301] mengerjakan soal Tugas Praktikum-1
dalam mata kuliah DPBO untuk keberkahanNya maka saya tidak melakukan kecurangan 
seperti yang telah dispesifikasikan. Aamiin

<h3>Deskripsi</h3>
Sebuah Program python simulasi game dengan menerapkan konsep OOP (Kelas, Objek, dan Relasi antar kelas). 

<h3>Desain Program</h3>

![DPBOTP1-Halaman-1 (1)](https://github.com/WildanRaffians/TP1DPBO2024C2/assets/134181656/c9a13a83-8b1b-47e4-928f-3307c2655354)

Program ini memiliki 13 Kelas.
<ol>
  <li>
    Kelas Player menampung data player, terdapat idPlayer, namaPlayer, umur, dan karakter player.
  </li>
  <li>
    Kelas PlayerKarakter menampung data Karakter dari player, terdapat id, nama, gender, objek status, objek role, objek skill,objek senjata dan list objek item. Juga terdapat method tambah_item, melawan_musuh, dan gunakan_skill.
  </li>
  <li>
    Kelas Status menampung data status karakter, seperti idstatus, level, max hp, hp saat ini (%), atk, def.  
  </li>
  <li>
    Kelas Senjata menampung data senjata, seperti idsenjata, tipe senjata (pedang, panah, dll), nama, jml kenaikan atk (setiap senjata pasti menaikkan atk), stat bonus (dapat berupa hp/def/atk, setiap senjata berbeda), dan jml kenaikan stat bonus
  </li>
  <li>
    Kelas Skill menampung data senjata, seperti idskill, nama, efek, deskripsi efek, cooldown (skill dapat digunakan setiap sekian(cooldown) detik sekali)
  </li>
  <li>
    Kelas NPC menampung data npc, seperti idnpc, nama, job.
  </li>
  <li>
    Kelas NiceNPC anak dari kelas NPC menampung data nicenpc, seperti data npc, list objek itemdijual, dan list objek misi
  </li>
  <li>
    Kelas EnemyNPC anak dari kelas NPC menampung data enemynpc, seperti data npc, objek status, objek skill, list objek drop item, dan statHidup (indikator masih hidup atau tidak)
  </li>
  <li>
    Kelas Misi menampung data misi, seperti idmisi, nama, deskripsi, list objek hadiah dan status (indikator sudah selesai atau belum), juga method sedang_dikerjakan
  </li>
  <li>
    Kelas Item menampung data item, seperti iditem, nama, deskripsi, jumlah
  </li>
  <li>
    Kelas Item Dijual anak dari item menampung data item dijual, seperti data item, harga, dan status(indikator habis atau belum)
  </li>
  <li>
    Kelas Wilayah menampung data wilayah, seperti id, nama, list objek item, list objek nice npc, list objek enemy.
  </li>
  <li>
    Kelas Tabel menampung data tabel, seperti baris dan kolom, juga terdapat method buat_tabel, pemisah_baris, buat_tabel_notif, dan buat_tabel_status.
  </li>
</ol>

Pada bagian main, berupa simulasi game, yang mana kita akan membuat karakter terlebih dahulu seperti menentukan namanya, role, skill dan senjatanya. 
Lalu akan ada pilihan menu untuk berpetualang, seperti cari NPC, cari Item di wilayah, cari musuh di wilayah, pindah wilayah, lihat status, lihat item yg dimiliki.
jika kita berinteraksi dengan NPC baik, ada kemungkinan NPC baik tersebut akan memberikan misi dan ketika kita selesai menyelesaikan misi maka kita akan mendapat hadiah.
NPC baik juga terkadang menjual beberapa barang.
Kita juga dapat melawan musuh, dan ketika menang kita akan mendapat item drop dari musuhnya.
