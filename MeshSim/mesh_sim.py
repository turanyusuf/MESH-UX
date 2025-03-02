from random import randint
import time

def mesh_signal():
    return f"Mesafe: {randint(1, 10)} metre"

while True:
    print(mesh_signal())
    time.sleep(2)
