from random import randint
import time

def zemin_algilama():
    mesafe = randint(0, 30)  # 0-30 cm arası rastgele mesafe
    if mesafe < 5:
        print("Adımını Kaldır Yusuf!")
    elif mesafe < 15:
        print("Engel Yaklaşıyor!")
    else:
        print(f"Güvenli Yolda, Mesafe: {mesafe} cm")

while True:
    zemin_algilama()
    time.sleep(2)
