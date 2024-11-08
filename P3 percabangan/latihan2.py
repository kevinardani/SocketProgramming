def tampilkan_deret_kuadrat(n):
    deret = [i**2 for i in range(1, n+1)]
    return deret

# Menampilkan deret kuadrat dari 1 hingga 9
n = 9
hasil = tampilkan_deret_kuadrat(n)

print("Deret kuadrat:")
print(", ".join(map(str, hasil)))