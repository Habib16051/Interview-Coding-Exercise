def is_palindrome(s):
    # covert the string into lowercase in order to avoid the case sensitivity
    s = s.lower()
    # Remove non-alphanumeric characters
    s = ''.join(i for i in s if i.isalnum())
    # Check if the string is equal to its reverse
    return s == s[::-1]

check = input('Enter your string to check: ')

if is_palindrome(check):
    print('The string is  a palindrome')
    
else:
    print('The string is not a palindrome')
  