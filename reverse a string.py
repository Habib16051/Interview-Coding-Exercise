def reverse_string(s):
    if len(s) == 0:
        return s
    
    else:
        return reverse_string(s[1:]) + s[0]
    
    

input_str = input('Enter your string: ')

result = reverse_string(input_str)
print('The reverse string is: ', result)