from time import time

alpha1 = 'abcdefghijklmnopqrstuvwxyz'
alpha2 = alpha1.upper()
alpha3 = '0123456789'
alpha4 = '"!@#$%*()_+-=§:?;/ªº°><.,\|'

alphabet = alpha1 + alpha2 + alpha3 + alpha4
y = len(alphabet)
n = 0

def Q4():
    test = input('senha : ')
    resu = y ** 4
    come = float(time())
    for i in alphabet:
        for i2 in alphabet:
            for i3 in alphabet:
                for i4 in alphabet:
                    x = (i + i2 + i3 + i4)
                    #print(x)
                    if x == test:
                        fim = float(time())
                        final = fim - come
                        print("senha {} testada".format(x))
                        print("levou {:.6f} segundos".format(final))
                        #print(resu)
                        break



def numero():
    test = int(input('senha : '))
    n = 0
    come = float(time())
    while n < test:
        n += 1
        #print(n)
    fim = float(time())
    final = fim - come
    print("senha {} testada".format(test))
    print("levou {:.6f} segundos".format(final))


numero()
    
