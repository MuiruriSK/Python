#type error
# Uncommenting the following line will raise a TypeError
# print("Hello" + 5)  # TypeError: can only concatenate str (not "int") to str

#type conversion
num_char = len(input("What is your name?"))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

a  = float(123)
print(type(a))
print(a)

print(70 + float("100.5"))

print(str(70) + str(100))