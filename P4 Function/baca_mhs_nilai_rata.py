def baca_data_nilai():
    nilai_mhs = []
    try:
        with open('nilai_mhs.txt', 'r') as f:
            for line in f:
                if line.strip():  # Memastikan baris tidak kosong
                    nama, nilai = line.strip().split(',')
                    nilai_mhs.append({'nama': nama, 'nilai': int(nilai)})
    except FileNotFoundError:
        print("File nilai_mhs.txt tidak ditemukan.")
    return nilai_mhs

def tampil_table(nilai_mhs):
    if not nilai_mhs:  # Cek jika list kosong
        print("Data nilai mahasiswa tidak ada.")
        return
    print(f"{'Nama':<10}{'Nilai':<5}")
    print("-" * 15)
    for data in nilai_mhs:
        print(f"{data['nama']:<10}{data['nilai']:<5}")

def rata_rata(nilai_mhs):
    if not nilai_mhs:  # Cek jika list kosong
        print("Tidak ada data untuk dihitung rata-ratanya.")
        return 0
    total = sum([data['nilai'] for data in nilai_mhs])
    avg = total / len(nilai_mhs)
    return avg

# Membaca data dari file
nilai_mhs = baca_data_nilai()
print(nilai_mhs)

# Menampilkan data dalam format tabel
tampil_table(nilai_mhs)

# Menghitung dan menampilkan nilai rata-rata
avg = rata_rata(nilai_mhs)
if avg > 0:  # Hanya menampilkan jika ada data
    print(f'Rata-rata nilai = {avg:.1f}')