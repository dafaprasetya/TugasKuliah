from time import sleep #import sleep untuk jeda waktu
import os #import os untuk menggunakan terminal

#Membuka file soal
try : #mencoba menjalankan script dibawah
    soal1 = open('soal1.txt', 'r') #membuka file soal1.txt
    soal2 = open('soal2.txt', 'r') #membuka file soal2.txt
except :  #jika gagal jalankan script dibawah
    soal1 = open('pertemuan2/soal1.txt', 'r') #membuka file soal1.txt 
    #pertemuan2 adalah nama folder
    soal2 = open('pertemuan2/soal2.txt', 'r') #membuka file soal2.txt

def tugasm1(): #membuat fungsi tugas mandiri 1 
    print(soal1.read()) #print isi soal1.txt
    brt = 5 #berat telur per kg
    hrg = 26000 #harga telur per kg
    ongkos = 3500 * 2 #ongkos pulang pergi
    uang = 200000 #uang ibu
    
    sisa = uang - ((brt * hrg) + ongkos) #sisa uang ibu
    
    print("Sisa uang ibu = {:,}".format(sisa)) #print sisa uang ibu

def  tugasm2(): #membuat fungsi tugas mandiri 2
    print(soal2.read()) #print isi dari soal2.txt
    hrg = int(input('Harga mangga per kg: ')) #harga mangga per kg(bentuk input)
    brt = int(input('Berat mangga yang dibeli (kg): ')) #berat mangga yang dibeli per kg (bentuk input)
    
    byr = hrg * brt #harga total / harga yang dibayar pembeli
    print('Total yang harus dibayar = {:,}'.format(byr)) # print harga total / harga yang dibayar pembeli

os.system('clear') #Clear Terminal

while True: #looping while
    
    pil = int(input("pilih soal :\n1. Tugas Mandiri 1\n2. Tugas Mandiri 2\nPilih :")) #pilihan user untuk memilih

    if pil == 1 : #kalau user memilih 1
        tugasm1() #jalankan function tugas mandiri 1
        print('\n') #garis baru
    elif pil == 2 : #kalau user memilih 2 
        tugasm2() #jalankan function tugas mandiri 2
        print('\n') #garis baru
        
    else: #jika user memilih selain angka yang diatas
        print('Gaada..') #print gaada
        
    print('kembali ke menu dalam 5 dtk') 
    sleep(5)

