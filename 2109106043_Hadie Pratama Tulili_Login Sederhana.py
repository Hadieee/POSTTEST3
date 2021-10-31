import os

class user:
    	Nama=()
    	Password=()


pilih = 0
DataUser = []

def menu():
	os.system('cls')
	print("============================\nMenu Program Data user\n============================")
	print("1. Buat akun baru user")
	print("2. Tampilkan akun user yang ada")
	print("3. Login")
	print("4. Keluar dari program")
	pilih = int(input("Masukkan pilihan anda : "))
	if pilih == 1 :
		pilih1()
		menu()
	elif pilih == 2:
		tampil()
		input("Kembali ke menu utama")
		menu()

	elif pilih == 3:
		os.system('cls')
		login()

	
	elif pilih == 4 :
		os.system('cls')
		print("================================================\nTerimakasih telah menggunakan program ini :)\nSemoga harimu menyenangkan!\n================================================")
		exit()

def tampil():
	os.system('cls');
	print("DATA AKUN USER")
	for data in DataUser:
		print("Nama : "+str(data.nama)) 
		print("Nama Akun User : "+str(data.username))
		print("Password :"+str(data.password))
		print("===================")

def pilih1():
	ulang = 'Y'
	while ulang in('y', 'Y'):
		os.system('cls')
		akun = user() 
		print("INPUT DATA USER ") 
		akun.nama = (str(input("Masukkan Nama User : "))) 
		akun.username = (str(input("Masukkan Nama Akun User : ")))
		akun.password = (str(input("Masukkan Password User : ")))
		DataUser.append(akun) 
		ulang = input("Data user telah berhasil disimpan!\nApakah Anda Ingin Mengulang (Y/ T)?")		

def login():
	percobaan = 0
	while percobaan < 3 :
		Nama = (str(input("Masukkan Username user : ")))
		Password = (str(input("Masukkan Password user : ")))
		for data in DataUser:
			if Nama == data.username and Password == data.password :
				print("Login berhasil !!!")
				input("Kembali ke menu utama")
				menu()
			elif Nama != data.username or Password != data.password :
				print("Username atau Password yang user masukkan salah\nSilahkan coba lagi")
				percobaan += 1
				if percobaan >= 3 :
					print("Maaf, anda telah gagal login sebanyak 3x\nProgram akan berakhir")
					exit()
menu()