tezlik = {
    "Tesla": 250,
    "BMW": 240,
    "Mercedes": 260,
    "Audi": 230
}

tezliklar = []
for t in tezlik.values():
    tezliklar.append(t)


for i in range(len(tezliklar)):
    max_tezlik = max(tezliklar) 
    for mashina in tezlik:
        if tezlik[mashina] == max_tezlik:
            print(mashina, ":", max_tezlik)
            tezliklar.remove(max_tezlik) 
            break