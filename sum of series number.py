def sum_of_series(n):
    return n * (n+1)//2

numbers = int(input('Enter the number of series: '))

if numbers < 0:
    print('Please Enter a Positive number')
    
else:
    
    result = sum_of_series(numbers)
    print(f'The sum of series is: ', result)