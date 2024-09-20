x,y = 0,0

n_cmd = int(input("Banyak perintah: "))
coordinate = f"Jalur yang ditempuh meong bross adalah ({x},{y})"

for i in range(n_cmd):
    cmd = input("Masukkan perintah: ")

    if cmd == "U":
        y += 1
        coordinate += f"-({x},{y})"
    elif cmd == "S":
        y -= 1
        coordinate += f"-({x},{y})"
    elif cmd == "T":
        x += 1
        coordinate += f"-({x},{y})"
    elif cmd == "B":
        x -= 1
        coordinate += f"-({x},{y})"
    elif cmd == "HOME":
        break
    else:
        coordinate += f"-({x},{y})"
        continue
    
print(coordinate)