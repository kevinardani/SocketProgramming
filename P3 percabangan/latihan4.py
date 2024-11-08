def nilai_huruf(nilai_angka):
    if nilai_angka >= 80:
        return 'A'
    elif nilai_angka >= 70:
        return 'B'
    elif nilai_angka >= 60:
        return 'C'
    elif nilai_angka >= 50:
        return 'D'
    else:
        return 'E'

mata_kuliah = []
while True:
    nama_mk = input("Masukkan nama mata kuliah (atau 'selesai' untuk mengakhiri): ")
    if nama_mk.lower() == 'selesai':
        break
    sks = int(input("Masukkan jumlah SKS: "))
    nilai_angka = float(input("Masukkan nilai angka: "))
    nilai_huruf_mk = nilai_huruf(nilai_angka)
    mata_kuliah.append((nama_mk, sks, nilai_angka, nilai_huruf_mk))

print("\nNama MK | SKS | Nilai Angka | Nilai Huruf")
print("-" * 40)
for mk in mata_kuliah:
    print(f"{mk[0]:<8} | {mk[1]:<3} | {mk[2]:<11} | {mk[3]:<11}")