# an important part of exception handling is when you have multiple functions calling each other like the program below

def get_day(user_info):
  day = int(input('What is the day of your bday? '))
  user_info.append(day)

def get_month(user_info):
  month = int(input('What is the month (1-12) of your bday? '))
  user_info.append(month)

def get_year(user_info):
  year = int(input('What is the year of your bday? '))
  user_info.append(year)

def get_user_bday(user_info):
    try:
      get_day(user_info)
      get_month(user_info)
      get_year(user_info)
      print('So your bday is', user_info)
    except ValueError:
      print('You entered incorrect data, bye!')

print('Hi, I will collect some info about your bday!')
user_info = []
get_user_bday(user_info)

# a single try-except statement is used to handle all exceptions raised for all function because of the rule:
    # 'exceptions are propagated through functions in python'
    # if a function that raises an exception doesn't have a try-except block, the exception is propagated to the function that called it..
    # ..until there is a tr-except block somewhere in the function call chain
    # if no try-except block specified anywhere, python will output an error