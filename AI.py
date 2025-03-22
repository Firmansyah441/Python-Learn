import random

responses = [
    "Oh, itu menarik! 🤔",
    "Bisa kamu jelaskan lebih lanjut? 🤖",
    "Hmm, saya setuju! 👍",
    "Menurut saya, itu keren! 🚀",
    "Kenapa begitu? 🤨"
]

print("Bot: Halo! Ngobrol yuk. (Ketik 'exit' untuk keluar)")
while True:
    user_input = input("Kamu: ")
    if user_input.lower() == "exit":
        print("Bot: Sampai jumpa! 👋")
        break
    print("Bot:", random.choice(responses))
