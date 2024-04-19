#Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.
#list
directors = ['lang', 'scott', 'hitchcock', 'donen']
#tuple
actors = ('gable', 'pacino', 'bardem', 'isaac')
#float
price = 90.99
#integer
temperature = -10
#decimal
from decimal import Decimal
ticket = 20.687
#dictionary
dictionary = {
    "table": "mesa",
    "chair": "silla",
    "Lamp": "lampara",
    "door": "puerta"
}
print(directors)
print(actors)
print(price)
print(temperature)
print(ticket)
print(dictionary)

#Exercise 2: Round your float up.
import math
bill = 4.29
print(math.ceil(bill))

#Exercise 3: Get the square root of your float.

print(math.sqrt(bill))

#Exercise 4: Select the first element from your dictionary.

dictionary = {
    "table": "mesa",
    "chair": "silla",
    "Lamp": "lampara",
    "door": "puerta"
}
room = dictionary.get('table')
print(room)

#Exercise 5: Select the second element from your tuple.
actors = ('gable', 'pacino', 'bardem', 'isaac')
print(actors[1])

#Exercise 6: Add an element to the end of your list.
directors = ['lang', 'scott', 'nolan', 'donen']
directors.extend(['eastwood'])
print(directors)

#Exercise 7: Replace the first element in your list.
directors = ['lang', 'scott', 'hitchcock', 'donen']
replace_first_element = directors.pop(0)
print(replace_first_element)
print(directors)

#Exercise 8: Sort your list alphabetically.
directors = ['lang', 'scott', 'hitchcock', 'donen']
directors.sort()
print(directors)

#Exercise 9: Use reassignment to add an element to your tuple.
actors = ('gable', 'pacino', 'bardem', 'isaac')
actors +=('grant', )
print(actors)
