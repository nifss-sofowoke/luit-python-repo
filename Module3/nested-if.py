# an if statement can be created in another if statement

answer_a = input('Do you like travelling? y/n: ')
if answer_a == 'y':
    answer_b = input('And do you like Asia? y/n: ')
    if answer_b == 'y':
        print('Excellent! You can win a ticket to Thailand!')
    else:
        print('Sorry to hear that!')
else:
    print('Sorry to hear that!')
    
# indentation is very important when nesting the other if
# 4 spaces btw 2nd if and answer b
# 5 spaces for print
