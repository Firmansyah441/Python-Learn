import cv2
import mediapipe as mp


cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# berfungsi untuk mengangkat jari kaya cek
def is_finger_up(landmarks, finger_tip, finger_dip):
    return landmarks[finger_tip].y < landmarks[finger_dip].y

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1) #frame bisa di atur
    h, w, _ = frame.shape
    
    # mengatur warna
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)
    
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            landmarks = hand_landmarks.landmark

            # jari
            is_index_up = is_finger_up(landmarks, 8, 6)    # Telunjuk
            is_middle_up = is_finger_up(landmarks, 12, 10) # Jari tengah
            is_ring_up = is_finger_up(landmarks, 16, 14)   # Jari manis
            is_pinky_up = is_finger_up(landmarks, 20, 18)  # Kelingking
            is_thumb_up = is_finger_up(landmarks, 4, 2)    # Jempol

            if is_index_up and not is_middle_up and not is_ring_up and not is_pinky_up:
                text = "WOII!"
            elif is_middle_up and not is_index_up and not is_ring_up and not is_pinky_up:
                text = "FUCK YOU!"
            elif is_index_up and is_middle_up and is_ring_up and is_pinky_up and is_thumb_up:
                text = "HELLO!"
            else:
                text = ""

            # Gambar garis tangan
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS, mp_draw.DrawingSpec(color=(0, 255, 0), thickness=3))

            # Tampilkan teks di layar
            if text:
                cv2.putText(frame, text, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)

    # Tampilkan frame gambar nya
    cv2.imshow("sensor tangan simple", frame)

    # Pencet q buat keluar
    if cv2.waitKey(1) & 0xFF == ord('f'):
        break

cap.release()
cv2.destroyAllWindows()

# # Import library yang diperlukan
# import cv2  # OpenCV untuk menangani video dan gambar
# import mediapipe as mp  # Mediapipe untuk mendeteksi tangan dan jari secara real-time

# # Inisialisasi kamera
# cap = cv2.VideoCapture(0)  # Membuka kamera utama (0 = kamera default)

# # Inisialisasi modul MediaPipe Hands untuk mendeteksi tangan
# mp_hands = mp.solutions.hands  # Modul untuk mendeteksi tangan
# hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)  
# # min_detection_confidence = tingkat kepercayaan dalam mendeteksi tangan
# # min_tracking_confidence = tingkat kepercayaan dalam melacak tangan

# # Inisialisasi modul untuk menggambar titik tangan
# mp_draw = mp.solutions.drawing_utils  

# # Fungsi untuk mengecek apakah jari terangkat
# def is_finger_up(landmarks, finger_tip, finger_dip):
#     """
#     Mengecek apakah jari dalam posisi terangkat.
#     Jika koordinat y ujung jari lebih kecil dari sendi jari, maka dianggap terangkat.
#     """
#     return landmarks[finger_tip].y < landmarks[finger_dip].y

# # Loop utama untuk menangkap video secara real-time
# while cap.isOpened():
#     ret, frame = cap.read()  # Membaca frame dari kamera
#     if not ret:
#         break  # Jika tidak berhasil membaca, keluar dari loop
    
#     frame = cv2.flip(frame, 1)  # Membalik gambar agar tampilan sesuai dengan gerakan kita
#     h, w, _ = frame.shape  # Mengambil ukuran frame (tinggi, lebar)

#     # Konversi warna dari BGR ke RGB karena Mediapipe menggunakan format RGB
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#     # Proses frame untuk mendeteksi tangan
#     result = hands.process(rgb_frame)

#     # Jika ada tangan yang terdeteksi
#     if result.multi_hand_landmarks:
#         for hand_landmarks in result.multi_hand_landmarks:  # Loop untuk setiap tangan yang terdeteksi
#             landmarks = hand_landmarks.landmark  # Mengambil titik koordinat tangan
            
#             # Mengecek apakah jari-jari terangkat
#             is_index_up = is_finger_up(landmarks, 8, 6)    # Telunjuk
#             is_middle_up = is_finger_up(landmarks, 12, 10) # Jari tengah
#             is_ring_up = is_finger_up(landmarks, 16, 14)   # Jari manis
#             is_pinky_up = is_finger_up(landmarks, 20, 18)  # Kelingking
#             is_thumb_up = is_finger_up(landmarks, 4, 2)    # Jempol

#             # Menentukan teks berdasarkan posisi jari
#             if is_index_up and not is_middle_up and not is_ring_up and not is_pinky_up:
#                 text = "WOII!"  # Jika hanya telunjuk yang terangkat
#             elif is_middle_up and not is_index_up and not is_ring_up and not is_pinky_up:
#                 text = "FUCK YOU!"  # Jika hanya jari tengah yang terangkat
#             elif is_index_up and is_middle_up and is_ring_up and is_pinky_up and is_thumb_up:
#                 text = "HELLO!"  # Jika semua jari terangkat
#             else:
#                 text = ""  # Jika tidak ada gerakan yang dikenali, kosongkan teks

#             # Gambar garis tangan dan titik-titik pada jari
#             mp_draw.draw_landmarks(
#                 frame, 
#                 hand_landmarks, 
#                 mp_hands.HAND_CONNECTIONS, 
#                 mp_draw.DrawingSpec(color=(0, 255, 0), thickness=3)  # Warna hijau, ketebalan 3
#             )

#             # Menampilkan teks pada layar jika ada yang dikenali
#             if text:
#                 cv2.putText(frame, text, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)
#                 # Parameter:
#                 # - (50, 100) = posisi teks pada layar
#                 # - cv2.FONT_HERSHEY_SIMPLEX = jenis font
#                 # - 2 = ukuran font
#                 # - (0, 0, 255) = warna merah (BGR format)
#                 # - 4 = ketebalan teks

#     # Tampilkan frame hasil deteksi
#     cv2.imshow("Sensor Tangan Simple", frame)

#     # Keluar dari program jika tombol 'f' ditekan
#     if cv2.waitKey(1) & 0xFF == ord('f'):
#         break

# # Setelah loop berakhir, lepaskan kamera dan tutup semua jendela OpenCV
# cap.release()
# cv2.destroyAllWindows()

