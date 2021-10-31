import os

Weekdays = ['Senin','Selasa','Rabu','Kamis','Jumat']
Weekend = ['Sabtu','Minggu']

pilihan="y"
while pilihan=="y":
    os.system('cls')
    print("""
    ==============================
    
             Tasty Coffe
              List Menu 
 
    ==============================
    A. Nasi Goreng   : Rp 20.000
    B. Mie Goreng    : Rp 20.000
    C. ES Kopi Hitam : Rp 11.000
    D. ES Kopi Susu  : Rp 11.000
    E. ES Kopi Coklat: Rp 12.000

    ==================================================================

                             !!!Diskon List!!!

    ==================================================================
    
    1. Mendapat Diskon setiap Pembelian 3 Minuman sebesar 10%
    2. Mendapat Diskon setiap Pembelian 2 Makanan sebesar 5%
    3. Mendapat Diskon setiap pembayaran melalui E-money sebesar 5%
    4. Mendapat Diskon saat weekend sebesar 5%
    5. Mendapat Diskon saat weekdays sebesar 10%


    ==================================================================
    """)
    pesan=str(input("masukkan list abjad menu ="))
    jumlahpesan=int(input("masukkan jumlah pesanan ="))
    if pesan == 'a':
        listnama= "Nasi Goreng"
        harga=(20000*jumlahpesan)
        ppn= int(harga * 0.1)
        if jumlahpesan >= 2:
            diskon = int(harga*0.05)
            totalharga=int((harga-diskon)+ppn)
        
        else:
            diskon =0
            totalharga=int(harga+ppn)
    elif pesan == 'b':
        listnama= "Mie Goreng"
        harga = (20000*jumlahpesan)
        ppn = int(harga * 0.1)
        if jumlahpesan >= 2:
            diskon = int(harga * 0.05)
            totalharga =int((harga-diskon)+ppn)

        else:
            diskon =0
            totalharga =int(harga+ppn)
    elif pesan == 'c':
        listnama= "ES Kopi Hitam"
        harga=int(11000*jumlahpesan)
        ppn = int(harga * 0.1)
        if jumlahpesan >= 3:
            diskon = int(harga*0.1)
            totalharga = int((harga-diskon)+ppn)

        else :
            diskon=0
        totalharga=int(harga+ppn)
    elif pesan == 'd':
        listnama= "ES Kopi Susu"
        harga=int(11000*jumlahpesan)
        ppn = int(harga * 0.1)
        if jumlahpesan >= 3:
            diskon = int(harga * 0.1)
            totalharga =int(harga-diskon+ppn)
        else :
            diskon = 0
            totalharga = int(harga+ppn)
    elif pesan == 'e':
        listnama= "ES Kopi Coklat"
        harga=int(12000*jumlahpesan)
        ppn = int(harga * 0.1)
        if jumlahpesan >= 3:
            diskon = int(harga * 0.2)
            totalharga =int((harga-diskon)+ppn)
        else :
            diskon = 0
            totalharga = int(harga+ppn)
    else:
        pilihan=input("menu tidak tersedia, silahkan masukkan abjad menu yang tersedia, silahkan ulangi kembali Y/N =")
        if pilihan == ('y', 'Y') :
            pilihan = 'y'

        elif pilihan == ('n', 'N') :
            print("======================================\nTerimakasih :) Silahkan datang kembali\n======================================")

    print("--------------------------")
    print("Tasty Coffe")
    print("--------------------------")
    print("Menu         :", listnama)
    print("Jumlah Pesan :", jumlahpesan)
    print("Harga        :", harga)
    print("Diskon       :", diskon)
    print("PPN          :", ppn)
    print("--------------------------")
    print("Jumlah Bayar :", totalharga)
    print("--------------------------")
    hari = str(input("Hari apa sekarang ? = "))
    if hari in Weekdays :
        print("--------------------------")
        print("Tasty Coffe")
        print("Hari :",hari)
        print("--------------------------")
        print("Menu :",listnama)
        print("Jumlah Pesan :", jumlahpesan)
        print("Harga :", harga)
        print("Diskon :", diskon+(harga*0.1))
        print("PPN :", ppn)
        print("--------------------------")
        print("Jumlah Bayar :", harga-diskon+(harga*0.1)+ppn)
        print("--------------------------")
        print("Anda mendapatkan diskon weekdays sebesar 10 % !!!")
        print("----------------------------------------------------")
        Bayar=input("Mau bayar pakai apa ? (Tunai, E-money) =")
        if Bayar == 'E-money' :
                print("--------------------------")
                print("Tasty Coffe")
                print("--------------------------")
                print("Menu :",listnama)
                print("Jumlah Pesan :", jumlahpesan)
                print("Harga :", harga)
                print("Diskon :", diskon+(harga*0.05*0.1))
                print("PPN :", ppn)
                print("--------------------------")
                print("Jumlah Bayar :", harga-diskon+(harga*0.05*0.1)+ppn)
                print("------------------------------------------------")
                print("Anda mendapatkan diskon weekdays sebesar 10 % Dan diskon E-money sebesar 5 % !!!")
    
        elif Bayar == 'Tunai' :
                print("--------------------------")
                print("Tasty Coffe")
                print("--------------------------")
                print("Menu :",listnama)
                print("Jumlah Pesan :", jumlahpesan)
                print("Harga :", harga)
                print("Diskon :", diskon+(totalharga*0.1))
                print("PPN :", ppn)
                print("--------------------------")
                print("Jumlah Bayar :", harga-diskon+(harga*0.1)+ppn)
                print("Anda mendapatkan diskon weekdays sebesar 10 % !!!")
                print("-------------------------------------------")

    elif hari in Weekend:
        print("--------------------------")
        print("Tasty Coffe")
        print("Hari :",hari)
        print("--------------------------")
        print("Menu :",listnama)
        print("Jumlah Pesan :", jumlahpesan)
        print("Harga :", harga)
        print("Diskon :", diskon+(harga*0.05))
        print("PPN :", ppn)
        print("--------------------------")
        print("Jumlah Bayar :", harga-diskon+(harga*0.05)+ppn)
        print("--------------------------")
        print("Anda mendapatkan diskon weekend sebesar 5% !!!")
        print("-------------------------------------------------")
        Bayar=input("Mau bayar pakai apa ? (Tunai, E-money) =")
        if Bayar == 'E-money' :
            print("--------------------------")
            print("Tasty Coffe")
            print("--------------------------")
            print("Menu :",listnama)
            print("Jumlah Pesan :", jumlahpesan)
            print("Harga :", harga)
            print("Diskon :", diskon+totalharga*0.05*0.05)
            print("PPN :", ppn)
            print("--------------------------")
            print("Jumlah Bayar :", harga-diskon+(harga*0.05*0.05)+ppn)
            print("--------------------------")
            print("Anda mendapatkan diskon weekend sebesar 5 % Dan diskon E-money sebesar 5 % !!!")
    
        elif Bayar == 'Tunai' :
            print("--------------------------")
            print("Tasty Coffe")
            print("--------------------------")
            print("Menu :",listnama)
            print("Jumlah Pesan :", jumlahpesan)
            print("Harga :", harga)
            print("Diskon :", diskon+(harga*0.05))
            print("PPN :", ppn)
            print("--------------------------")
            print("Jumlah Bayar :", harga-diskon+(harga*0.05)+ppn)
            print("Anda mendapatkan diskon weekend sebesar 5% !!!")
            print("--------------------------")

    pilihan=input("apakah anda ingin order kembali Y/N =")
    if pilihan == ('y', 'Y') :
        pilihan = 'y'

    elif pilihan == ('n', 'N') :
        print("======================================\nTerimakasih :) Silahkan datang kembali\n======================================")
else:
    os.system('cls')
    print("======================================\nTerimakasih :) Silahkan datang kembali\n======================================")