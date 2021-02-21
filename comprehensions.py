from os import makedirs, listdir
from os.path import splitext
from random import randint, choice
from string import ascii_lowercase

# Getting the numbers 1 through 100 in a list

numbers = []

for i in range(1, 101):
    numbers.append(i)

print(len(numbers))

[i for i in range(1, 101)]

[i**2 for i in range(1, 101)]

# Creating use Case for the Dictionary Comprehension
makedirs("txt_files")

ascii_lowercase

#testing if choice works with ascii_lowercase
choice (ascii_lowercase)

for i in range(10):
    choice_integer = randint(1, 50)
    new_str = ''
    for j in range(choice_integer):
        new_str += choice(ascii_lowercase)
    with open(f"txt_files/{new_str}.txt", "w") as my_file:
        my_file.write("File created")

#Method 1: Traditional Dictionary Addition
count_dict = {}

for i, file_name in enumerate(listdir("txt_files")):
    file_name = splitext(file_name)[0]
    count_dict[f"file_{i+1}"] = len(file_name)

count_dict.keys()
count_dict['file_1']
count_dict['file_10']

#Method 2: Dictionary Comprehension
count_dict_2 = {f"file_{i+1}": len(splitext(file_name)[0]) for i, file_name in enumerate(listdir("txt_files"))}

count_dict_2['file_1']
