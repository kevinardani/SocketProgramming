def baca_file_nilai(nama_file):
  data_mahasiswa = []

  with open(nama_file, 'r') as file:
    for line in file:
      nama, nilai = line.strip().split(',')
      data_mahasiswa.append({'nama': nama, 'nilai': int(nilai)})

  return data_mahasiswa

nama_file = "nilai_mhs.txt"  # Ganti dengan nama file Anda
data = baca_file_nilai(nama_file)
print(data)