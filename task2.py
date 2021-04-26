k = input("Введите предложение: ")

z = k.find(',')
if( z == -1):
    print('Нет запятых')
    exit(1)
f = k.find(',', z+1)
if(f != -1):
    print(k[z+1:f])
elif(f == -1):
    print(k[z+1:])
