"""
TODO:
1. Create list of favorite foods
2. Print first and last
3. Add one item
4. Remove one item
5. Print all items with loop
6. List comprehension for the lengths of each food item -
 create a new list where each item is  the length of the corresponding food item in the original list.
"""
# Create list of favorite foods
list_of_foods = ["apple", "peach", "plum"]
# Print first and last
print(list_of_foods[0], list_of_foods[-1])
# Add one item
list_of_foods.append("banana")
# Remove one item
list_of_foods.remove("apple")
# Print all items with loop
for food in list_of_foods:
    print(food)
# List comprehension for the lengths of each food item - create a new list where each item is  the length of the corresponding food item in the original list.
lengths = [len(food) for food in list_of_foods]
print(lengths)