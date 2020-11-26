times = ('Sport', 'Náutico', 'Santa Cruz', 'Salgueiro', 'Central',
         'Afogados', 'Vitória', 'Petrolina', 'América', 'Flamengo Arcoverde')
for t in range(0, len(times)):
    if (t >= 0 and t < 3):
        print(t+1, "º", times[t])
    if (t >= 6 and t <= 9):
        print(t+1, "º", times[t])

print("Times em ordem alfabética: ", sorted(times))
for t in range(0, len(times)):
    if times[t] == 'Vitória' in times:
        print("Posição do Vitória: ", t+1, "ª")
