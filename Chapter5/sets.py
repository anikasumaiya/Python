# A set is a collection of unordered and unique items , mutable
# set automatically  removes duplicate items and written in curly braces

languages =  {"C++", "python", "Ruby", "Java", "Javascript", "python"}

print(languages)

print(type(languages))

empty_set = {}
# empty_set = set()
print(empty_set)

set1 = {1, 2, 3, 4, 4}
set2 = {2, 3, 4}
set3 = {5, 6}

print(set1)

print(set1.union(set2,set3))

print(set3.intersection(set2,set1))

print(set1.intersection(set2))