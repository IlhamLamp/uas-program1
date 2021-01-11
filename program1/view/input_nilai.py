# Menginput data
def input_nama():
    global nama
    nama = input("Masukkan nama : ")
    return nama


def input_nim():
    global nim
    nim = input("Masukkan nim  : ")
    return nim


def input_ntugas():
    global n_tugas
    n_tugas= input("Masukkan nilai tugas : ")
    return n_tugas


def input_nuts():
    global n_uts
    n_uts  = input("Masukkan nilai uts   : ")
    return n_uts


def input_nuas():
    global n_uas
    n_uas  = input("Masukkan nilai uas   : ")
    return n_uas


# Nilai akhir
def nakhir():
    global n_akhir
    n_akhir= int(n_tugas)*30/100 + int(n_uts)*35/100 + int(n_uas)*35/100
    return n_akhir
