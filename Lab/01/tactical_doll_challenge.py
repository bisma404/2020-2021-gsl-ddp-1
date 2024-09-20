print("### MY TACTICAL DOLL ###")

tact_doll_name = input("Masukkan nama Tactical Doll: ")
tact_doll_firepower = int(input("Masukkan Firepower: "))
tact_doll_rof = int(input("Masukkan Rate of Fire: "))
tact_doll_acc = int(input("Masukkan Accuracy: "))
tact_doll_eva = int(input("Masukkan Evasion: "))

tact_doll_dps = round((tact_doll_firepower * tact_doll_rof) / 60, 2)
tact_doll_combat = int(round(30 * tact_doll_firepower + 40 * (tact_doll_rof**2) / 120 + 15 * (tact_doll_acc + tact_doll_eva), 0))

print("\n### ENEMY TACTICAL DOLL ###")

enemy_doll_name = input("Masukkan nama Tactical Doll: ")
enemy_doll_firepower = int(input("Masukkan Firepower: "))
enemy_doll_rof = int(input("Masukkan Rate of Fire: "))
enemy_doll_acc = int(input("Masukkan Accuracy: "))
enemy_doll_eva = int(input("Masukkan Evasion: "))

enemy_doll_dps = round((enemy_doll_firepower * enemy_doll_rof) / 60, 2)
enemy_doll_combat = int(round(30 * enemy_doll_firepower + 40 * (enemy_doll_rof**2) / 120 + 15 * (enemy_doll_acc + enemy_doll_eva), 0))

print("\n### RESULT ###")
print(tact_doll_name)
print("Damage per Second:", tact_doll_dps)
print("Combat Effectiveness:", tact_doll_combat)
print()
print(enemy_doll_name)
print("Damage per Second:", enemy_doll_dps)
print("Combat Effectiveness:", enemy_doll_combat)
print()

if tact_doll_dps >= enemy_doll_dps and tact_doll_combat >= enemy_doll_combat:
    print("Keputusan: Gass lawan")
else:
    print("Keputusan: Kabuuur")