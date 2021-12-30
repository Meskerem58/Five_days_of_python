#string formating 
country= 'Ethiopia'
City= 'Addis ababa'
gravity = 9.81
mass= 66 # mass in kg
print('%s is in Africa' % ('Ethiopia'))
print ('%.2f is the gravetitional is %.')

#this is the better way of formating string 

print(f'the gravity {gravity} and the mass is {mass} in kg and the {country}')


#I am Asabeneh Yetayeh. I live in Helsinki, Finland. I teach Python. My skills are HTML, CSS, JS, and Python. I am 250 years old. 

#I am Meskeem Debeb. I live in Seattle , Wa, . I learn Python. My skills are edting ,excel 
first_name = 'Meskerem'
last_name = 'Debeb'
age = 100
city= 'seattle'
skills = ['Edititng', 'Excel','python', 'reading' ,'playing']
country = 'USA'
learn_lang= 'Python' 
first_skills = ', '.join(skills[0:-1])
print(f'My name is {first_name} {last_name}. I live in {country}  {city} .  Now I am learning {learn_lang}. I am {age} years old.My skills are {first_skills}.')
first_skills = ', '.join(skills[0:-1])

nums = [1, 2 ,4,7,8, 9]
print(nums[:])
print(' ,' .join(['Ethiopia', 'Seattle' ,'Addis' , 'Ketema']))