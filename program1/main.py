import os, platform
from model.daftar_nilai import *
from view.input_nilai import *
from view.view_nilai import *


if(platform.system() == 'Windows'):
    os.system('cls')
else:
    os.system('clear')

while(True):

    print(" "*15,"======================================")
    print(" "*15,'|              PROGRAM               |')
    print(" "*15,'|       DAFTAR NILAI MAHASISWA       |')
    print(" "*15,"======================================")
    tanya = int(input("\n[0]Tambah , [1]Tampilkan , [2]Hapus , [3]Ubah , [4]Cari , [5]Keluar : "))
    print("\n")

    if(tanya == 0):
        tambah_data()

    elif(tanya == 1):
        cetak_daftar_nilai()

    elif(tanya == 2):
        hapus_data()

    elif(tanya == 3):
        ubah_data()

    elif(tanya == 4):
        cari_data()

    elif(tanya == 5):
        break

    else:
        print("Keyword yang anda masukkan salah ...")

    print("\n")
