#Program Mengurutkan Angka

def jumlah(x):
    list = []
    b_angka = int(input("Banyak Angka yang ingin di masukkan : "))
    while x < b_angka: 
        angka = int(input("masukkan angka :"))
        list.append(angka)
        print(list)
        x = x+1
       
    else:
        list.sort()
        print("\nHasil Sortir")
        print(list)
        l = (len(list))
        list.pop(0)
        list.remove(max(list))
        print("\nHasil Sortir selanjutnya")
        print(list)
        print("\nprogram selesai")

jumlah(0)