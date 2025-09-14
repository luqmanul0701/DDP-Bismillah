# Nama : Dliya Syahla Hariyanto
# Nim : 2509116095
# minpro 

daftar_reservasi=[]
while True:
    print("-----Sistem Reservasi Nail Art-----")
    print("1.Tambah data")
    print("2.lihat data")
    print("3.edit data")
    print("4.hapus data")
    print("5.keluar")

    menu = input("Pilih menu (1/2/3/4/5) : ")

    if menu=="1":
        nama=input("nama: ")
        layanan=input("layanan: ")
        harga=input("harga: ")
        tanggal=input("tanggal: ")
        jam=input("jam: ")
        daftar_reservasi=[(nama,layanan,harga,tanggal,jam)]
        print("data berhasil di tambah")

    elif menu=="2":
        if daftar_reservasi:
            print("data sekarang: ",daftar_reservasi)
        else:
            print("belum ada data")
            
    elif menu=="3":
            if daftar_reservasi:
                edit = input("edit data? y/n: ")
                if edit =="y":
                    nama=input("nama baru: ")
                    layanan=input("layanan baru: ")
                    harga=input("harga baru: ")
                    tanggal=input("tanggal baru: ")
                    jam=input("jam baru: ")
                    daftar_reservasi=[(nama,layanan,harga,tanggal,jam)]
                    print("data berhasil diedit")
                else:
                    print("belum ada data yang di edit")

    elif menu=="4":
            if daftar_reservasi:
                hapus = input("hapus data? y/n : ")
                if hapus =="y":
                 daftar_reservasi=[]
                print("data berhasil di hapus")
            else:
                print("tidak ada data di hapus")

    elif menu=="5":
        print("kelua")
        break
    else:
        print("menu tidak ada")


                    









    
        







