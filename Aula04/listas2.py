herois = list()
personagens = list()
herois.append("Mistica")
herois.append("Marvel")
print(herois)

personagens.append(herois[:])
print(personagens)
herois.append("Mulher Maravilha")
herois.append("DC")
personagens.append(herois[2:])
# print(personagens)
print(personagens[1][1])

'''
print(personagens[0][0])

print(personagens[1])
# print(herois[0])
# print(herois[1])
# print(herois[2])
# print(herois[3])
'''
