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

# Membaca data dari file
nilai_mhs = baca_data_nilai()
print(nilai_mhs)

# Menampilkan data dalam format tabel
tampil_table(nilai_mhs)