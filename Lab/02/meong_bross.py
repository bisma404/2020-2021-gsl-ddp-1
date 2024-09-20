x,y = 0,0

n_cmd = int(input("Banyak perintah: "))

for i in range(n_cmd):
    cmd = input("Masukkan perintah: ")

    if cmd == "U":
        y += 1
    elif cmd == "S":
        y -= 1
    elif cmd == "T":
        x += 1
    elif cmd == "B":
        x -= 1
    elif cmd == "HOME":
        break
    else:
        continue

print(f"Karakter Meong Brosss berada di koordinat ({x},{y})")