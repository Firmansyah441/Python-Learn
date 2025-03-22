print("Pikirkan angka 1-10, lalu saya akan menebaknya! 🔮")
input("Tekan ENTER jika sudah siap...")

low, high = 1, 10

while low <= high:
    guess = (low + high) // 2  # Teknik pencarian biner (lebih akurat)
    response = input(f"Apakah angkamu {guess}? (y/l/h): ").lower()

    if response == "y":
        print(f"Saya berhasil menebak! Angka kamu adalah {guess}! 🎉")
        break
    elif response == "l":
        high = guess - 1  # Kurangi batas atas
    elif response == "h":
        low = guess + 1  # Tambah batas bawah
    else:
        print("Masukkan 'y' untuk benar, 'l' jika terlalu tinggi, 'h' jika terlalu rendah.")
