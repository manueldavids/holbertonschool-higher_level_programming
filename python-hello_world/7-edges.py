#!/usr/bin/python3
word = "Holberton"

# 1. Get the first 3 letters
word_first_3 = word[:3]           # 'Hol'

# 2. Get the last 2 letters
word_last_2 = word[-2:]           # 'on'

# 3. Get everything except the first and last letter
middle_word = word[1:-1]          # 'olberto'

# 4. Print the results
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")
