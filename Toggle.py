string = input("Enter a string: ")
new_string = str()

for i in string:
    if i.isupper():
        i = i.lower()
        new_string += i
    else:
        i = i.upper()
        new_string += i
print("Toggled string:", new_string)
