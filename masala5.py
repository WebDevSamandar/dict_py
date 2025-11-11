mashina_soni = {
    "Chevrolet" : 120,
    "Toyota" : 95,
    "BMW" : 60,
    "KIA" : 75
}


eng_kop = max(mashina_soni, key = mashina_soni.get)
eng_kam = min(mashina_soni, key = mashina_soni.get)

print("Eng ko'p sotilgan mashina:",eng_kop)
print("Eng kam sotilgan mashina:",eng_kam)