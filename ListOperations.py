fruits=["apple","banana","orange"]
print(fruits)       # Output: ['apple', 'banana', 'orange']
fruits.insert(1,"grape")
print(fruits)       # Output: ['apple', 'grape', 'banana', 'orange']
fruits.remove("banana")
print(fruits)       # Output: ['apple', 'grape', 'orange']
fruits.append(['kiwi','mango'])
print(fruits)       # Output: ['apple', 'grape', 'orange', ['kiwi', 'mango']]
print(len(fruits))   # Output: 4
fruits.pop()
print(fruits)       # Output: ['apple', 'grape', 'orange', 'kiwi']
fruits.clear()
print(fruits)       # Output: []