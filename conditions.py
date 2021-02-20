# test 3 letters and based on if statements return the correct response

letter1='m'
letter2='u'
letter3='y'

vowels='aeiou'

if letter1 in vowels:
    print(f"{letter1} is a vowel.")
elif letter1=='y':
    print(f"{letter1} is a y.")
else: 
    print(f"{letter1} is a consonant.")
    
if letter2 in vowels:
    print(f"{letter2} is a vowel.")
elif letter2=='y':
    print(f"{letter2} is a y.")
else: 
    print(f"{letter2} is a consonant.")
    
if letter3 in vowels:
    print(f"{letter3} is a vowel.")
elif letter3=='y':
    print(f"{letter3} is a y.")
else: 
    print(f"{letter3} is a consonant.")