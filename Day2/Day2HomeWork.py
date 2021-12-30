# Q.1 Concatenate the string 'Thirty', 'Days', 'Of

python_bootcumb = [ ' Thirty ', ' Days ' , ' Of ' , ' Python ']
str_concat = '' .join(python_bootcumb)
print (str_concat)

# Q.2 Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
code = [ 'Coding' ,' For' , ' All']
code_concat = '' .join(code)
print(code_concat)

# Q.3 Declare a variable named company and assign it to an initial value "Coding For All".
company = 'Coding For all'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.title())
print(company.swapcase())
# Q.9 
all_words = company.split()
first_word = all_words[0]
print(first_word)
print(company.replace('Coding', 'Python'))
# Q. 14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
it_company = ['Facebook ',',' 'Google ',',' 'Microsoft ',',' 'Apple ',',' 'IBM ',',' 'Oracle',',' 'Amazon ']
#print(it_company)
it_company_concat = '' .join(it_company)
print(' The list of IT companies in the world are ,',it_company_concat)
# Q. 15  What is the character at index 0 in the string Coding For All.
print(company.index(str(-1)))