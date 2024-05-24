#МЕТОДИ РЯДКА
our_string = "Hello world"

# print(our_string.upper()) #HELLO WORLD
# print(our_string.lower()) #hello world
# print(our_string.count("o")) #2
# print(our_string.count("ll")) #1
# print(our_string.count("l", 3)) #2
# print(our_string.count("l", 3, 7)) #1
# print(our_string.find("wor")) #6
# print(our_string.find("o")) #4
# print(our_string.rfind("o")) #7
# print(our_string.find("g")) #-1
# print(our_string.index("g")) #ValueError: substring not found
# print(our_string.replace("Hello", "hi")) #hi world
# print(our_string.replace(" ", "")) #Helloworld
# print(our_string.isalpha()) #False
# print("sdasad".isalpha()) #True
# print("1233".isdigit()) #True
# print("text".rjust(10)) #      text
# print("test".rjust(10, "&")) #&&&&&&test
# print("text".ljust(12, "!")) #text!!!!!!!!
new_string= "    hi    "
# print(new_string.strip()) #hi
# print(new_string.lstrip()) #hi
# print(new_string.rstrip()) #    hi
print(our_string)
our_string = our_string.upper()
print(our_string)

