def nilai_huruf(nilai_angka):
    if nilai_angka >= 80:
        return 'A', 4.0
    elif nilai_angka >= 70:
        return 'B', 3.0
    elif nilai_angka >= 60:
        return 'C', 2.0
    elif nilai_angka >= 50:
        return 'D', 1.0
    else:
        return 'E', 0.0

mata_kuliah = []
total_sks = 0
total_bobot = 0

while True:
    nama_mk = input("Masukkan nama mata kuliah (atau 'selesai' untuk mengakhiri): ")
    if nama_mk.lower() == 'selesai':
        break
    sks = int(input("Masukkan jumlah SKS: "))
    nilai_angka = float(input("Masukkan nilai angka: "))
    nilai_huruf_mk, bobot = nilai_huruf(nilai_angka)
    mata_kuliah.append((nama_mk, sks, nilai_angka, nilai_huruf_mk))
    total_sks += sks
    total_bobot += sks * bobot

print("\nNama MK | SKS | Nilai Angka | Nilai Huruf")
print("-" * 40)
for mk in mata_kuliah:
    print(f"{mk[0]:<8} | {mk[1]:<3} | {mk[2]:<11} | {mk[3]:<11}")
ipk = total_bobot / total_sks if total_sks > 0 else 0
print(f"\nIPK: {ipk:.2f}")