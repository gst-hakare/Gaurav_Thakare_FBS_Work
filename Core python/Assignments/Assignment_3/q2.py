# Q Write a program to input any alphabet and check whether it is vowel or consonant.

alphabet = input('Enter a alphabet : ')

vowels = 'a','e','i','o','u','A','E','I','O','U' 

if alphabet in vowels:
    print(f'{alphabet} is a vowel.')
else:
    print(f'{alphabet} is consonant.')