'''
list = [1,2,3,4,5,6,7,8,9]
list2 = [11,12,13,14,15,16,17,18,19,20]
print("list of number from 1-10:", list);
print("list of number from 10-20:", list2);
print("list of number start from 1 to 4:",list[:4]);
print("list of number start from 5 to 6:",list[4:6]);
print("list of number start from 5 to end:",list[4:]);
print("list of number start from 1 to 6:",list[:6]);
list.append(10)
print("list of number from 1-10 after append:",list)
list.extend(list2)
print("list of number from 1-20 after extend list and list2:",list);
#in python we can change the number by letter
list[1]= 'CHANGE'
list[10] = 'UGWENO'
list[16] = 'KILIMANJARO'
print('list of number from 1-10 and change the fisrt number to C:',list);

languages = ['SWIFT','JAVA','DART','PYTHON']
for language in languages:
  print (language);

student_ID= {112,113,114,115,116,117,118,119,120}
print('Student ID:',student_ID);
vowel_letter = {'a','e','i','o','u'}
print("Vowel letter:", vowel_letter)
mixed_string={112,'A','b','Hello','Bye'}
print("mixed String:", mixed_string)
vowel_letter.update(mixed_string)
print('Updated vowel letter List: ',vowel_letter)
print(len(vowel_letter))

a= {1,2,3,4,5}
b= {2,3,6,7,8,9,10}
print('union of set a and set b', a.union(b))
print('intersection of set a and set b', a.intersection(b))
print('difference of set a and set b', a.difference(b))
print('symmetric_difference of set a and set b', a.symmetric_difference(b))
if a==b:
 print('set a is equal to b')
else:
 print('set a and set b are not equal')
 capital_city ={'Dodoma': 'Tanzania', 'Nairobi':'Kenya'}
 print('Capital city of the country',capital_city)
 capital_city['Bujumbura'] = 'Burundi'
 capital_city[55] = 56
 print('Updated capital city of country', capital_city)

 string1 = ('PYTHON')
 print(string1)
 string2 = ('I love Python-Programming Language')
 print(string2)
 message = """
 I love programmimg
 PYTHON
JAVA
DART
"""
print(message)
print(len(message))

'''

# Create an empty list called my_list
my_list = []

# Append the following elements to my_list: 10, 20, 30, 40
my_list.extend([10, 20, 30, 40])

# Insert the value 15 at the second position in the list
my_list.insert(1, 15)

# Extend my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])

# Remove the last element from my_list
my_list.pop()

# Sort my_list in ascending order
my_list.sort()

# Find and print the index of the value 30 in my_list
index_30 = my_list.index(30)
print("Index of 30 in my_list:", index_30)