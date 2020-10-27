#/usr/bin/python3
from itertools import *

"""CHAIN"""
# chain() facilita el procesamiento de varias secuencias sin construir una lista grande.
for i in chain([1, 2, 3], ['a', 'b', 'c']):
    print(i, end=' ')
print()

def make_iterables_to_chain():
    yield [1, 2, 3]
    yield ['a', 'b', 'c']

for i in chain.from_iterable(make_iterables_to_chain()):
    print(i, end=' ')
print()


"""ZIP"""
for i in zip([1, 2, 3], ['a', 'b', 'c']):
    print(i)