from Countries_list import countries
from pprint import pprint 

pprint(countries)
new_list =[]
for country in countries:
    new_list.append([country, country.upper(),country.upper()[:3],len(country)])
pprint(new_list) 

def countires_with_land():
    new_list= []
    for c in countries:
         if 'land' in c:
            new_list.append(c)
    return new_list
print(countires_with_land()) 


        
    
        
