from model.daftar_nilai import mahasiswa

def cetak_daftar_nilai():
#menampilkan daftar mahasiswa
    print("Daftar Nilai:")
    print("===========================================================================")
    print("| No |         Nama         |     NIM     | Tugas |  UTS  |  UAS  | Akhir |")
    print("===========================================================================")
    no = 1
    if len(mahasiswa.values()) > 0:
        for item in mahasiswa.values():
            print("| {0:2} | {1:20} | {2:11} | {3:5} | {4:5} | {5:5} | {6:5.2f} |".format
                 (no, item[0],
                  item[1], item[2],
                  item[3], item[4],
                  item[5]
                 ))
            no += 1
        print('---------------------------------------------------------------------------')
    else:
        print("|",'{:^71}'.format("TIDAK ADA DATA"),"|")
        print("===========================================================================")

# Cari
def cetak_hasil_pencarian():
    print("Mencari data: ")
    print("=================================================")
    nama = input("Masukan nama untuk mencari data: ")
    if nama in data.keys():
        print('\nHasil')
        print("Nama: {0}\nNIM : {1}\nNilai Tugas: {2}\nUTS: {3}\nUAS: {4}\nNilai akhir: {5:.2f}"
              .format(nama, mahasiswa[nama][1],
                            mahasiswa[nama][2], mahasiswa[nama][3],
                            mahasiswa[nama][4], mahasiswa[nama][5]))
    else:
        print("'{}' tidak ditemukan.".format(nama))
