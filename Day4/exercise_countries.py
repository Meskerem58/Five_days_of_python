from countries_data import countries_data
from pprint import pprint
#pprint(countries_data)
for c in countries_data:
    print(c['name'], c['capital'], c['population'] )
population = []
for country in countries_data:
    population.append(country['population'])
    #sorted
""" sorted_counties= sorted(population , reverse= True)
top_ten_counties= sorted_counties[:10]
print(top_ten_counties) """

top_10= sorted(countries_data, key =lambda c:c['population'], reverse= True)[:10]
pprint(top_10)

#COUNT THE NUMBER OF LANGUAGE 
#COUNT THE TOTAL NUMBER OF LANGUSGE
#REMOVE THE DUPLICATE 



