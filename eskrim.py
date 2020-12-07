import time
def countdown(t=5):
    print("Aplikasi akan mati dalam waktu :")
    while t > 0:
        print(t)
        t -= 1
        time.sleep(1)

eskrim = ["coklat","stroberi"]
hargaes = ["2000","5000"]
topping = ["cochochips","popcorn"]
hargatop = ["1000","3000"]

def admin():
    auth = (input("Masukan Password sebagai admin : "))
    if auth == "123":
        while True :
            esbaru = eskrim.append(input("Masukan Rasa Eskrim Baru >> "))
            esharga = hargaes.append(input("Masukan Harga Eskrim Baru >> "))
            topingbaru = topping.append(input("Masukan Topping Baru >> "))
            topharga = hargatop.append(input("Masukan Harga Toping Baru >> "))
            pesan = (input("Apakah kamu ingin menambah eskrim lagi ? y/n >> "))
            if pesan == "y":
                continue
            else:
                break
    else:
        print("Kau bukan ADMIN !!!!!")
        countdown()
        exit()

def pesan():
    while True :
      print("="*50)
      saldo = 6000
      print (f"Anda memiliki saldo sebesar {saldo} ")
      print("="*50)
      print ("Rasa Eskrim Yang tersedia :")
      print(" Eskrim"+ " "*6 +"Harga")
      for i in range(len(eskrim)):
         x1 = i;x1 += 1
         print(x1, eskrim[i] + " "*6 +hargaes[i])
    #   for x in range(len(eskrim)):
    #         x1 = x;x1 += 1
    #         print (x1,eskrim[x])
      print ("")
      print ("Pilihan Toping :")
      print("   Topping"+ " "*6 +"Harga")
      for x in range(len(topping)):
            x1 = x;x1 += 1
            print (x1,topping[x]+ " "*6 +hargatop[i])
      print ("="*50)

      pilihes = int(input("Pilih Jenis Eskrim mu >> "))
      pilihes -= 1
      pilihtoping = int(input("Pilih Jenis toppingmu >> "))
      pilihtoping -= 1
      total = (int(hargaes[pilihes])) + (int(hargatop[pilihtoping]))
      print("="*50)
      print("Eskrim mu adalah",eskrim[pilihes],"dengan toping",topping[pilihtoping],"dengan jumlah total yang harus dibayar adalah ",total)
      bayar = input(f"Anda memiliki saldo sebesar {saldo} Apakah anda ingin membayar  y/n? ")
      if bayar == "y":
          if saldo < total:
              print("Saldo Kamu Kurang")
          else:
              print("Pembayaran berhasil")
      else:
          print("Pembayaran di cancel, silahkan pesan lagi")
      ulang = input("Apakah Kamu mau pesan lagi ? Y/N >> ")
      if ulang == "y":
        continue
      else:
        break
    print ("Terima Kasih")
    countdown()

print("Selamat Datang di Rumah Eskrim ")
user= (input("Anda Sebagai : \n 1. Admin \n 2. Pelanggan \n Jawab dengan angka >> "))
if user == "1":
    admin()
    print("="*50)
    tanya = input("Apakah kamu mau pesan y/n >> ")
    if tanya == "y":
        pesan()
    else:
        countdown()
        exit()
else:
    pesan()