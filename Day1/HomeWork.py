# The name of the dictionar is person. 
# It will have the follwing keys first name, last name, age, marital status, skills,
#  hobbies, brothers, sisters, parents, country, state, address, favorite quote
# keys should be string 

person = {
'first_name': 'Meskerem',
'last_name': 'Debeb' ,
'favourite_food' : 'Shiro',
'place_want_to_visit': 'Paris' ,
'skills': {'editing','excel'} , 
'hobbie': ' watching_home_decor_viedos' ,
'country': 'USA' ,  'state': 'WA', 
'favorite_quote': 'Do a small thing with a great love',
'sisters': ('Mazi' , 'TG' ,'Alem ' ),
'brothers' :('Abu' ,'Ayale' , 'Addis' ),
'address': {'street': 'Kenmore' ,
'zipcode': '98133'
}
}

for key,value in person.items():
	print(key, ':', value)








