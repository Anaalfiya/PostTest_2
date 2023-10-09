from prettytable import PrettyTable

menu = {
    "klinik"  : ["Perawatan Wajah"],
    "harga": [50000]
}

data = PrettyTable()


def tables():
    data.title = 'KLINIK KECANTIKAN'
    data.field_names = ["No","klinik","Harga"]
    data.clear_rows()
    if len(menu['klinik']) <= 0:
        print("Data Kosong")
    else:
        for i in range(len(menu['klinik'])):
            data.add_row([i + 1,menu['klinik'][i],menu['harga'][i]])
        print(data)
    

def admin(): 
    print("1. Liat menu Kecantikan")
    print("2. Tambah menu Kecantikan")
    print("3. Edit menu Kecantikan")
    print("4. Hapus menu Kecantikan")
    print("5. Logout")
    pilih = input("Masukan Pilihan Menu : ")
    while True:
        if pilih == "1":
           
            tables()
            ulang = input("Apakah anda ingin mengulang ya / tidak : ")
            if ulang.lower() == "ya" or ulang.lower() == "y" :
               admin()
            else: raise SystemExit
        elif pilih == "2":
           
            tables()
            klinikBaru = input("Masukan Nama klinik : ")
            hargaBaru = int(input("Masukan Harga Baru : "))
            if klinikBaru in menu['klinik']:
               
                print("Nama klinik Sudah ada")
                ulang = input("Apakah anda ingin mengulang ya / tidak : ")
                if ulang.lower() == "ya" or ulang.lower() == "y" :
                   admin()
                else: raise SystemExit
            else:
                menu['klinik'].append(klinikBaru)
                menu['harga'].append(hargaBaru)
                tables()
                print("Data Berhasil Ditambahkan")
                ulang = input("Apakah anda ingin mengulang ya / tidak : ")
                if ulang.lower() == "ya" or ulang.lower() == "y" :
                    admin()
                else: raise SystemExit
        elif pilih == "3":
           
            tables()
            pilih = int(input("Masukan Nomor Pilihan Anda : "))
            pilih  -= 1
           
            print("Anda mengedit data : ",menu['klinik'][pilih])
            klinikBaru = input("Masukan Nama klinik Baru : ")
            hargaBaru = int(input("Masukan Harga Baru : "))
            menu['klinik'][pilih] = klinikBaru
            menu['harga'][pilih] = hargaBaru 
            tables() 
            ulang = input("Apakah anda ingin mengulang ya / tidak : ")
            if ulang.lower() == "ya" or ulang.lower() == "y" :
                admin()
            else: raise SystemExit
        elif pilih == "4":
           
            tables()
            pilih = int(input("Masukan Nomor Pilihan Anda Yang Ingin Dihapus: "))
            pilih -=1 
            menu.get('klinik').pop(pilih)
            menu.get('harga').pop(pilih)
            ulang = input("Apakah anda ingin mengulang ya / tidak : ")
            if ulang.lower() == "ya" or ulang.lower() == "y" :
                admin()
            else: raise SystemExit
        elif pilih == "5":
            main()
        else:
           
            admin()

def pasien():
    pilih = input("Apakah Anda Ingin Membeli? ya / tidak : ")
    if pilih.lower() == "ya" or pilih.lower() == "y":
        pilihan = int(input("Nomor Yang Ingin Dibook: "))
        pilihan -=1
        print("Anda Membooking : ",menu['klinik'][pilihan])
        print("Harga : ",menu['harga'][pilihan])
        print("Berhasil Membook")
        pasien()
    else:
        print("1.Logout")
        print("2.Exit")
        pilih = input("Masukan Pilihan: ")
        if pilih == "1":
            main()
        else:raise SystemExit

def main():
    print("Pilih Role Yang Sesuai")
    print("1.Admin")
    print("2.customer")
    role = input("Pilih Role Anda -> ")
    if role == "1":
        nama = input("Masukan Nama Anda: ")
        password = input("Masukan Password Anda: ")
        if nama == "admin" and password == "admin":
           
            admin()
    elif role == "2":
        tables()
        pasien()
    else:print("Invalid")

main()