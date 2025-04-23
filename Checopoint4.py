#Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.
from decimal import Decimal
exercise_one= [('one', 'two', 'three'), 15.1, 151, Decimal(1.51), {'one':1, 'two':2, 'three':3}]
print(exercise_one)


#Exercise 2: Round your float up.
import math

print(math.ceil(exercise_one[1]))

#Exercise 3: Get the square root of your float.
print(math.sqrt(exercise_one[1]))

#Exercise 4: Select the first element from your dictionary.
primero= exercise_one[4]

primer_valor=list(primero.items())[0]
print(primer_valor)

#Exercise 5: Select the second element from your tuple.

segundo= exercise_one[0]
segundo_valor=segundo[1]
print(segundo_valor)

#Exercise 6: Add an element to the end of your list.

exercise_one += ['four']
print(exercise_one)

#Exercise 7: Replace the first element in your list.

exercise_one[0] =  ('uno', 'dos', 'tres')
print(exercise_one)

#Exercise 8: Sort your list alphabetically.
#I have created a list for this exercise because in exercise_one the list I have created includes a tuple, a float... and I can`t sort it alphabetically.

exercise_eight = ['uno', 'dos', 'tres', 'cuatro']
exercise_eight.sort()
print(exercise_eight)

#Exercise 9: Use reassignment to add an element to your tuple.
exercise_nine = exercise_one[0]
exercise_nine += ('cuatro',)
print(exercise_nine)
