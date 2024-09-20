# Mubah code input
mubah = list(input("Masukkan string: "))

# Calculate sum of all digits and remove them from the list
counter = sum(int(char) for char in mubah if char.isnumeric())
mubah = [char for char in mubah if not char.isnumeric()]

# Shift each letter by 'counter' positions
for char in range(len(mubah)):
    decode = ord(mubah[char]) + counter
    if (ord(mubah[char]) - ord('a')) < 0:
        decode = (decode - ord('A')) % 26 + ord('a') if decode > ord('Z') else (decode - ord('A')) % 26 + ord('A')
    else:
        decode = (decode - ord('a')) % 26 + ord('A') if decode > ord('z') else (decode - ord('a')) % 26 + ord('a')
    mubah[char] = chr(decode)

mubah_decrypt = "".join(mubah)

# Output the decrypted string
print(mubah_decrypt)