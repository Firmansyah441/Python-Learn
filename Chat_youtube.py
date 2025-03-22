import pytchat
import datetime

VIDEO_ID = "L7csDwlJTZ8" 
chat = pytchat.create(video_id=VIDEO_ID)

print("****** persib day 📺 ****** \n")
print("🔴 Mengambil chat dari YouTube Live...\n")
 
while chat.is_alive():
    for c in chat.get().sync_items():
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {c.author.name}: {c.message}")

