marvel = ["Homem-Aranha", "Hulk", "Viúva Negra", "Pantera Negra"]
marvel[3] = "Vampira"
# print(marvel)
# marvel.append("Tempestade")
#print('p1: ', marvel)
# marvel.append("Vampira")
marvel.append("Vampira")
marvel.insert(4, "Mística")

#print('p2: ', marvel)
#del marvel[3]
# marvel.pop()
#marvel[4] = "Vampira"
# marvel.remove('Vampira')
#print('p3: ',marvel)
# marvel.remove('Vampira')
#print('p4: ',marvel)
# marvel.pop()

print("antes de remover ", marvel)
for h in range(0, len(marvel)):
    if 'Vampira' in marvel:
        marvel.remove('Vampira')
print(marvel)
