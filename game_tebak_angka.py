import random

number = random.randint(1, 100)
guess = None

print("🎮 Selamat datang di game Tebak Angka! (1-100)")
while guess != number:
    guess = int(input("Tebak angka: "))
    if guess < number:
        print("Terlalu kecil! 🔽")
    elif guess > number:
        print("Terlalu besar! 🔼")
    else:
        print("🎉 Benar! Angkanya adalah", number)
