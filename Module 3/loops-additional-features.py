# additional features of loops 

# special python instruction that doesn't do anything
# pass

for i in range(11):
    pass

# the pass instruction is used because the loop syntax requires at least one instruction inside the loop body
# prevents code form outputing an error
# used in cases where you don't know what instruction to add to your code

# nested loops
for a in range(1,6):
    for b in range(1, 6):
         print(a, 'x', b, '=', a * b)
         
# loops with else statements
# rarely used
i = 2
while i < 5:
    print(i)
    i += 1
else:
    print('else:', i)

# the else branch of a loop is always exceuted exactly once
# exception: break statement