print("### REQUEST TACTICAL DOLL ###")

tact_doll_name = input("Masukkan nama Tactical Doll: ")
tact_doll_firepower = int(input("Masukkan Firepower: "))
tact_doll_rof = int(input("Masukkan Rate of Fire: "))
tact_doll_acc = int(input("Masukkan Accuracy: "))
tact_doll_eva = int(input("Masukkan Evasion: "))

tact_doll_dps = round((tact_doll_firepower * tact_doll_rof) / 60, 2)
tact_doll_combat = int(round(30 * tact_doll_firepower + 40 * (tact_doll_rof**2) / 120 + 15 * (tact_doll_acc + tact_doll_eva), 0))

print("\n### SUCCESS ###")
print("Tactical Doll:", tact_doll_name)
print("Firepower:", tact_doll_firepower)
print("Rate of Fire:", tact_doll_rof)
print("Accuracy:", tact_doll_acc)
print("Evasion:", tact_doll_eva)
print("Damage per Second:", tact_doll_dps)
print("Combat Effectiveness:", tact_doll_combat)