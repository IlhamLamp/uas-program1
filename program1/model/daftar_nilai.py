from view.input_nilai import *

mahasiswa = {}
#menambah daftar mehasiswa
def tambah_data():
    global mahasiswa
    print("Masukkan data mahasiswa . . .")
    nama   = input_nama()
    nim    = input_nim()
    n_tugas= input_ntugas()
    n_uts  = input_nuts()
    n_uas  = input_nuas()
    n_akhir= nakhir()

    mahasiswa[nama] = [nama, nim, n_tugas, n_uts, n_uas, n_akhir]
    print("-> Data berhasil di tambah!")

#menghapus daftar mahasiswa
def hapus_data():
    nama = input("Masukkan nama untuk menghapus : ")
    if nama in mahasiswa.keys():
        del mahasiswa[nama]
        print("-> Daftar Mahasiswa {} telah di hapus".format(nama))
    else:
        print("-> Mahasiswa {} tidak ditemukan".format(nama))

#mengubah daftar mahasiswa
def ubah_data():
    nama = input("Masukkan nama mahasiswa untuk merubah data : ")
    if nama in mahasiswa.keys():
        print("-> Mau merubah apa ?")
        tanya = input("-> (semua), (nim), (tugas), (uts), (uas) : ")
        if tanya.lower() == "semua":
            print("+++ Mulai mengubah data {} +++".format(nama))
            mahasiswa[nama][1] = input("Ubah NIM  : ")
            mahasiswa[nama][2] = input("Ubah nilai tugas : ")
            mahasiswa[nama][3] = input("Ubah nilai uts   : ")
            mahasiswa[nama][4] = input("Ubah nilai uas   : ")
            mahasiswa[nama][5] = int(mahasiswa[nama][2])*30/100 + int(mahasiswa[nama][3])*35/100 + int(mahasiswa[nama][4])*35/100
            print("-> Data berhasil diubah!")
        elif tanya.lower() == "nim":
            mahasiswa[nama][1] = input("Ubah NIM : ")
            print("-> NIM berhasil diubah!")
        elif tanya.lower() == "tugas":
            mahasiswa[nama][2] = input("Ubah nilai tugas : ")
            mahasiswa[nama][5] = int(mahasiswa[nama][2])*30/100 + int(mahasiswa[nama][3])*35/100 + int(mahasiswa[nama][4])*35/100
            print("-> Nilai tugas berhasil diubah!")
        elif tanya.lower() == "uts":
            mahasiswa[nama][3] = input("Ubah nilai uts :")
            mahasiswa[nama][5] = int(mahasiswa[nama][2])*30/100 + int(mahasiswa[nama][3])*35/100 + int(mahasiswa[nama][4])*35/100
            print("-> Nilai UTS berhasil diubah!")
        elif tanya.lower() == "uas":
            mahasiswa[nama][4] = input("Ubah nilai uas : ")
            mahasiswa[nama][5] = int(mahasiswa[nama][2])*30/100 + int(mahasiswa[nama][3])*35/100 + int(mahasiswa[nama][4])*35/100
            print("-> Nilai UAS berhasil diubah!")
        else:
            print("-> Keyword yang anda masukkan salah ...")
    else:
        print("-> Mahasiswa {} tidak ditemukan".format(nama))

# Mencari data mahasiswa
def cari_data():
    print("Mencari data: ")
    print("=================================================")
    nama = input("Masukan nama untuk mencari data: ")
    if nama in mahasiswa.keys():
        print('\nHasil')
        print("Nama: {0}\nNIM : {1}\nNilai Tugas: {2}\nUTS: {3}\nUAS: {4}\nNilai akhir: {5:.2f}"
              .format(nama, mahasiswa[nama][1],
                            mahasiswa[nama][2], mahasiswa[nama][3],
                            mahasiswa[nama][4], mahasiswa[nama][5]))
    else:
        print("'{}' tidak ditemukan.".format(nama))
