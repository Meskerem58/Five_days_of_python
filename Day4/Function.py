# what are functions?
# the built in function  like 'print' 
# custom function 
# we need functions becasue the function will be reasuable , sastunaible 


def add_two_nums( a, b):
    total = a + b
    return total
#print (add_two_nums(45, 87))


def add_three_nums( a, b ,c ):
    total = a+ b + c
    return total
#print(add_three_nums( 20,40, 50))


#****************************************

def calcu_area_rectangele(l, w):
    area = l * w
    return area
#print(calcu_area_rectangele(4, 6))

def calcu_parameter_of_rectangle( m, n):
    total = 2 *(m +n)
    return total
#print( calcu_parameter_of_rectangle(8, 9))


def create_fullname(first_name , last_name):
    #first_name = 'meski'
    #last_name = ' debeb'
    full_name=  first_name + last_name
    return full_name
#print(create_fullname('Meski', 'Debeb'))

def genrate_even_num(n):
    even= list(range(1, n + 1, 2 ))
    return even
#print(genrate_even_num(16))

def calcu_weight( mass , gravity = 9.81 ):
    weight = mass * gravity
    return weight
print(calcu_weight( 75))
print(calcu_weight( 75, 1.65))




 
