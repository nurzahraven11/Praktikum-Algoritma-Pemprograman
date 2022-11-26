#Tugas Akhir Praktikum Alogaritma Pemprograman

"""
Bayar Tagihan Listrik

""" 

import datetime

identitas = ["Nama pelanggan", "Alamat", "No Telepon", "Tanggal Dibuat", "IDPEL",
 "Rp Tag PLN", "biaya admin bank", "Total Bayar"]
data = []
biayaadminbank = {}
biayalayanan = {}
tanggal = datetime.datetime.now()

print(37*"="+"""
Nama\t : Nur Zahra Anggriyani
NIM\t : 2270211024
program\t : Pembayaran Listrik
""" + 37*"=" + "\n\n")

for x in range(len(identitas)):
    val = input("masukan" + identitas[x] + "\n->")

print(6*"=" + " Bon Tagihan Listrik " + 6*"=")
 

