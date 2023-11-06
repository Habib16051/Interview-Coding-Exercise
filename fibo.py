def fibo(n):
    if n < 0:
        return ('Incorrect Input')
    elif n == 0:
        return 0
    elif n == 1 or n==2:
        return 1
    
    else:
        # addition of previous two iterations
        return fibo(n-1) + fibo(n-2)  
    

num = int(input('Enter the Number: '))

result = fibo(num)

print(f'Fibonacci of {num} is {result}')