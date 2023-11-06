def fact(n):
    if n < 0:
        return 1
    elif n ==0 or n==1:
        return 1
    
    else:
        return n * fact(n-1)
    
num = int(input('Enter the number: '))

result = fact(num)


if num < 0:
    print('Factorial is not define for the negative number!')
    
else:
    print(f'factorial of {num} is {result}')
    