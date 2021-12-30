a = 50 
if a > 0:
    print (f'{a}  is postive ')
elif a == 0:
    print( f' {a} is negative ')
else:
    print( f' {a} Then is negative')


Weather = input(' what is the weather like today?')
if Weather == 'rainy':
    print('Please bring an umberella')
elif Weather =='snow':
    print( 'the day is couldy')
elif Weather == 'cloudy':
    print(' I like the day')
else:
    print(' The day is beautifull')


first_name = input( 'what is your first name? ')
last_name = input(' what is your last name? ')
year_born = int(input ( 'when were you born? '))
city = input ( 'what is the capital city ? ')
country = input( 'where are you from? ')
current_year = 2021

age = (current_year - year_born)
pronoun = 'She'
geneder  = input( "what is your gender? ").lower()

if geneder == 'Female':
    pronoun( 'She')


print(f'{pronoun} is {first_name} {last_name} {age} years old. {pronoun} came from {city} the capity of {country}.')


