# computers can do things based on conditions
# the 'if' statement is used in python for conditional statements

# examples
user_age = int(input('What is your age?'))
if user_age > 50:
    print('You are over 50 years old')
    print('Sorry, you do not qualify')
    
elif user_age == 50:
   print('You are exactly 50 years old')
   print('You will need to meet additional conditions to qualify') 
# two equal signs are used to check equality in python (used for the 'elif'function)
# unlike one equal sign which is used to assign variables

else: 
    print('You are 50 years old or younger')
    print('Congratulations, you qualify')
    
# all commands to be executed must be indented

if condition_a_met:
    do_scenario_a()
elif condition_b_met:
    do_scenario_b()
elif condition_c_met:
    do_scenario_c()
else:
    do_scenario_d()