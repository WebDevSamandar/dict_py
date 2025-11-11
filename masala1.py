cars = {
    "Malibu": 35000,
    "Spark": 12000,
    "Cobalt": 18000,
    "Trecker": 28000,
}

eng_qimmat = max(cars, key = cars.get)
eng_arzon = min(cars, key = cars.get)

ortacha = sum(cars.values()) / len(cars)

print("Eng qimmat:",eng_qimmat,"-",cars[eng_qimmat])
print("Eng arzon:",eng_arzon,"-",cars[eng_arzon])
print("O'rtacha narx:",int(ortacha))
