# função com parâmetro
def convert_seg(hora, minuto, segundo):
    result = (hora*3600)+(minuto*60)+segundo
    return result


#print(convert_seg(1, 1, 0))
h = 2
m = 3
s = 10
#print(convert_seg(h, m, s))
#print(convert_seg(hora=h, minuto=m, segundo=s))
#print(convert_seg(minuto=m, hora=h, segundo=s))


# vários parâmetros
def soma(*num):
    # print(type(num))
    j = 0
    for n in range(0, len(num)):
        j += num[n]
    return num


print(soma(1, 2, 3))
