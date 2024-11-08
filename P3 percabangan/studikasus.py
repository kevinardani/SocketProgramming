while True:
         angka = int(input("Masukkan angka (1-30) atau 0 untuk keluar: "))
         if angka == 0:
             print("Permainan berakhir")
             break
         elif 1 <= angka <= 10:
             print("Kau dekat dengan harta!")
         elif 11 <= angka <= 20:
             print("Kau jauh dari harta!")
         else:
             print("Kau sangat jauh dari harta!")
     