# DATA TYPE , NUMBERS( INT, FLOAT, COPLETX)
#STRINGS 
#integers --- 3, 2, -1, 0 ,
#float 
#BOOLEANS ( TRUE /FALSE)
# LIST , SET, TUBLE, DICTIONARY
# builtin function we use to checke type  
print(type(1+2j))
print(type(20))
print (type('10'))
print (type(9.81))

#numbers(int, float, complex)

#Strings
#can be short or many pages 
letter = 'a'
word = 'I love python. '
print(len(letter))
print(word[0])
#print(word(2))
last_index= len(word) -1 
print(word[last_index])
print(word[2:6])
sentence = 'I love python'
print(sentence.upper())
# .UPPER AND SO ON IS A METHOD 
#print(sentence.count())
dan = 'gggggggggggggggggggggsssssssssssssssssssmmmmmmmmmmmmmmmmmmrrrrrrrrrrrrrrfffffffffff'
total_count = len(dan)
print (dan)
g = dan.count('a')
s = dan.count ('s')
r = dan.count (' r')
print(g, s)
print ('proportion' , ' a nucotide:' , round(g /total_count * 100 , 2), '%')
# string methods 
#.upper(), .lower(), .count()
sentence = ' I love python.\n as I love JavaScript.\n I love shiro '
print(sentence.count('I'))
print(sentence.count('love'))
print(sentence.count("I love"))

#INDEX STARTS WITH 0
print(sentence.title())
print(sentence.startswith('I'))
print(sentence.rfind('1'))
#print(sentence.split(.)) to split the sentencese 
first_name = 'Meskerem' 
Last_name = 'Debeb'
print(sentence)
print('Meski\tage\tcountry')
print('we used to say \" an apple the day keep the doctur away"\'')