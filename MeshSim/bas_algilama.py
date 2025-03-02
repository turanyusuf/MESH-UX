from random import randint
import time

def bas_algilama():
    mesafe = randint(30, 150)  # 30 ile 150 cm arası
    if mesafe < 50:
        print("Başını Eğ Yusuf!")
    else:
        print(f"Güvenli Geçiş, Mesafe: {mesafe} cm")

while True:
    bas_algilama()
    time.sleep(2)
