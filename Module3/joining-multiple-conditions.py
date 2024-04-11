# to execute a code using multiple conditions, use boolean operators
# 3 boolean operators: and, or, not

# and
user_age = int(input('What is your age? '))
user_country = input('What is your country? ')

if user_age < 25 and user_country == 'Germany':
    print('You can apply for a German student exchange programme')
else:
    print('Sorry, you do not qualify')
 
# or   
user_country = input('What is your country?')
if user_country == 'Sweden' or user_country == 'Denmark' or user_country == 'Norway':
    print('You can apply for a Scandinavian student exchange programme')
else:
    print('Sorry, you do not qualify')
    
# not
user_country = input('Where do you come from? ')
if not user_country == 'Germany':
    print('you are not from Germany!')
else:
    print('you are from Germany')
# not negates the boolean value
# if the condition is true then it will turn it false

# joining all 3 operators
user_age = int(input('What is your age? '))
user_country = input('What is your country? ')

if ((not user_country == 'Germany') and user_age < 25) or \
   (user_country == 'Germany' and user_age < 23):
    print('You qualify!')
else:
    print('You don\'t qualify!')
    
# order of operations for boolean operators
# 1. not
# 2. and
# 3. or
    
