# Eligma code input
eligma = list(input("Masukkan string: "))

# Calculate sum of all digits and remove them from the list
counter = sum(int(char) for char in eligma if char.isnumeric())
eligma = [char for char in eligma if not char.isnumeric()]

# Shift each letter by 'counter' positions
eligma_decrypt = ''.join(
    chr((ord(char) - ord('a') + counter) % 26 + ord('a')) 
    for char in eligma
)

# Output the decrypted string
print(eligma_decrypt)