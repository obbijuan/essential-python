""" A list is made from zero or more elements, separated by commas and
surrounded by square brackets. """

""" This shows that values do not need to be unique. """
first_names = ['Graham', 'John', 'Terry', 'Terry', 'Michael']

randomness = ["Punxsatawney", {"groundhog": "Phil"}, "Feb. 2"]
leap_years = [2000, 2004, 2008]

""" Empty list. """
empty_list = list()

""" Converts a tuple to a list """
a_tuple = ('ready', 'fire', 'aim')
a_list = list(a_tuple)
print(a_list)

""" Create from a String with split() """
talk_like_a_pirate_day = '9/19/2019'
talk_like_a_pirate_day = talk_like_a_pirate_day.split('/')
print(talk_like_a_pirate_day)
# ['9', '19', '2019']


""" Get Items with a Slice """
marxes = ['Groucho', 'Chico', 'Harpo']

new_marxes = marxes[0:2]
print(new_marxes)
# ['Groucho', 'Chico']


""" Starts at the beginning and goes right by 2 """
new_marxes_2 = marxes[::2]
print(new_marxes_2)
# ['Groucho', 'Harpo']


""" Here, we start at the end and go left by 2 """
new_marxes_3 = marxes[::-2]
print(new_marxes_3)
# ['Harpo', 'Groucho']


""" Reverse a list """
reverse_marxes = marxes[::-1]
print(reverse_marxes)
# ['Harpo', 'Chico', 'Groucho']


""" The reverse() function changes the list but doesn’t return its value. """
marxes.reverse()
print(marxes)


""" Add an Item to the End """
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.append('Zeppo')
print(marxes)
# ['Groucho', 'Chico', 'Harpo', 'Zeppo']


""" Add an Item by Offset with insert() """
marxes.insert(2, 'Gummo')
print(marxes)
# ['Groucho', 'Chico', 'Gummo', 'Harpo', 'Zeppo']


"""Duplicate All Items with *"""
print(["blah"] * 3)
# ['blah', 'blah', 'blah']


""" Combine Lists by Using extend() """
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.extend(others)
print(marxes)
# ['Groucho', 'Chico', 'Harpo', 'Zeppo', 'Gummo', 'Karl']


""" If we had used append(), others would have been added 
as a single list item rather than merging its items """
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.append(others)
print(marxes)
# ['Groucho', 'Chico', 'Harpo', 'Zeppo', ['Gummo', 'Karl']]


""" Change an Item by [offset] """
marxes = ['Groucho', 'Chico', 'Harpo']
marxes[2] = 'Wanda'
print(marxes)
# ['Groucho', 'Chico', 'Wanda']


""" Change Items with a Slice """
numbers = [1,2,3,20,21,22]
numbers[3:5] = [8,9,10,11]
print(numbers)
# [1, 2, 3, 8, 9, 10, 11, 22]

numbers = [1, 2, 3, 4]
numbers[1:3] =  (98, 99, 100)
print(numbers)
# [1, 98, 99, 100, 4]

""" Delete an Item by Offset with del """
marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Karl']
del marxes[-1]
print(marxes)
# ['Groucho', 'Chico', 'Harpo', 'Gummo']

marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo']
del marxes[1]
print(marxes)

""" Delete an Item by Value with remove() """
marxes = ['Groucho', 'Harpo', 'Gummo']
marxes.remove('Harpo')
print(marxes)


""" Get an Item by Offset and Delete It with pop() """
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
marxes.pop(1)
print(marxes)
# ['Groucho', 'Harpo', 'Zeppo']

""" Find an Item’s Offset by Value with index() """
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes.index('Harpo'))
# 2
# If the value is in the list more than once, only the offset of the first one is returned.


""" The Pythonic way to check for the existence of a value in a list is using in. """
words = ['a', 'deer', 'a' 'female', 'deer']
print('deer' in words)
# True


""" Count Occurrences of a Value with count() """
snl_skit = ['cheeseburger', 'cheeseburger', 'cangreburger', 'cheeseburger']
print(snl_skit.count('cheeseburger'))
# 3

""" Convert a List to a String with join() """
separator = " | "
friends = ['Harry', 'Hermione', 'Ron']
joined = separator.join(friends)
print(joined)
# Harry | Hermione | Ron
separated = joined.split(separator)
print(separated)

""" Reorder Items with sort() or sorted() """
marxes = ['Groucho', 'Chico', 'Harpo']
sorted_marxes = sorted(marxes)
print(sorted_marxes)
# ['Chico', 'Groucho', 'Harpo']

marxes = ['Harpo', 'Groucho', 'Chico']
marxes.sort()
print(marxes)
# ['Chico', 'Groucho', 'Harpo']
