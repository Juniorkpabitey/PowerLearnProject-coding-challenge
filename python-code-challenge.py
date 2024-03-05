# Task 1: Sum of integers in a list
user_input = input("Enter a list of integers separated by spaces: ")
integer_list = list(map(int, user_input.split()))
sum_of_integers = sum(integer_list)
print(f"Sum of integers in the list: {sum_of_integers}")

# Task 2: Tuple of favorite books
favorite_books = ("Book 1", "Book 2", "Book 3", "Book 4", "Book 5")
print("Favorite Books:")
for book in favorite_books:
    print(book)

#Task 3: Dictionary for person information
person_info = {}
person_info['name'] = input("Enter your name: ")
person_info['age'] = input("Enter your age: ")
person_info['favorite_color'] = input("Enter your favorite color: ")
print("Person Information:")
print(person_info)

# Task 4: Common elements in sets
set1_input = input("Enter elements for the first set separated by spaces: ")
set2_input = input("Enter elements for the second set separated by spaces: ")
set1 = set(map(int, set1_input.split()))
set2 = set(map(int, set2_input.split()))
common_elements = set1.intersection(set2)
print(f"Common elements in both sets: {common_elements}")

# Task 5: List comprehension for words with odd number of characters
word_list = ["apple", "banana", "orange", "grape", "kiwi"]
odd_length_words = [word for word in word_list if len(word) % 2 != 0]
print("Words with odd number of characters:")
print(odd_length_words)
