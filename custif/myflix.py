#!/usr/bin/env python3
message = 'The book we recommend is '
print('select a number from the series? 1 true 3 will recomend a book')
connection = float(input())
if connection == 1:
    message = message + 'Harry Potter.'
elif connection == 2:
    message = message + 'Hobbit & Lord of the Rings.'
elif connection == 3:
    message = message + 'Chronicles of Narnia.'
else:
    message = message + 'Indiana Jones.'
print(message)
