kasblar = {
    "Bill Gates": "Dasturchi",
    "Cristiano Ronaldo" : "Futbolchi", 
    "Elon Musk" : "Tadbirkor", 
    "Messi" : "Futbolchi"
}

ism = input("Ismni kiriting: ")

if ism in kasblar:
    print(f"{ism}ning kasbi: {kasblar[ism]}")
else:
    print("Bunday ism topilmadi.")