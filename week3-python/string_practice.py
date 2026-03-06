

first_name = "Rashida"
last_name = "Ahmed"
age = 20
favorite_concept = "f-strings"
print("Task 1 Output:")
print(first_name)
print(last_name)
print(age)
print(favorite_concept)
print()  


full_name_plus = first_name + " " + last_name
print("Task 2 Output:")
print(full_name_plus)
full_name_fstring = f"{first_name} {last_name}"
print(full_name_fstring)
print()


print("Task 3 Output:")
print(full_name_fstring.upper())
print(full_name_fstring.lower())
a_count = full_name_fstring.lower().count('a')
print(f"Number of 'a' (any case): {a_count}")
space_index = full_name_fstring.find(" ")  
print(f"First space index: {space_index}")
coder_name = full_name_fstring.replace(first_name, "Coder")
print(coder_name)
print()


intro = f"Hi, I am {full_name_fstring} I am {age} years old and my favourite concept so far is {favorite_concept}."
print("Task 4 Output:")
print(intro)
print()


print("Task 5 Output:")
print(f"First char: '{full_name_fstring[0]}'")
print(f"Last char: '{full_name_fstring[-1]}'")
first_name_slice = full_name_fstring[:space_index]  
print(f"First name slice: '{first_name_slice}'")
