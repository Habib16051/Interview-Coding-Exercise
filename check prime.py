number = int(input('Enter a number: '))

if number > 1:
    for i in range(2, int(number/2) + 1):
        if (number % 2) == 0:
            print(f'{number} is not a primary number')
            break
    else:
        print(f'{number} is a primary number')
            
else:
    print(f'{number} is not a primary number')