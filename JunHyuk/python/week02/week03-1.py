layer = int(input('숫자를 입력하세요: '))

for i in range(layer):
    for j in range(i+1):
        print('*', end='')
    print()
