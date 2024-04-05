# break and continue influence how loop bodies are executed

# break instruction causes python to exit the loop and  moves on to the next instruction outside the loop
# break instructions are used inside a loop with if statements

while True:
    name = input('Enter your name or EXIT to close the program: ')
    if (name == 'EXIT'):
        break
    print('Hello', name)
    
# contiunue instruction is used to exit the current iteration and move on to the next one
# it is also used with if statements to skip a certain iteration

for i in range(1, 21):
    if i % 5 == 0:
        continue
    print(i)