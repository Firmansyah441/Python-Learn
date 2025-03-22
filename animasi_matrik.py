import random
import time

chars = "FirmanGanteng"
width = 80

columns = [0] * width

while True:
    print("".join(random.choice(chars) if random.random() > 0.9 else " " for _ in range(width)))
    time.sleep(0.05)
