#Lesson_2_and_3
#Введення інформації.Математичні дії.Зміна типу
#Повернення значень та assert
# var = 10
# new_var = bool(var)
# print(type(new_var), new_var)
# print()
#
# var_false = False
# var_true = True
# print(type(var_false), var_false)
# print(type(var_true), var_true)
# print()
#
# print(True and False) #False
# print(True and True) #True

# print(True or True) #True
# print(True or False) #True
# print(False or False) #False

# print(not True) #False
# print(not False) #True

# first_number = 193
# second_number = 193
# third_number = -193
# print(id(first_number))
# print(id(second_number))
# print(id(third_number))
#
# print( first_number is second_number) #True
# print(first_number is third_number) #False
# print( second_number is third_number) #False

# print(first_number == second_number) #True
# print(first_number == 93) #False

# print(first_number != second_number) #False
# print(first_number != 93) #True

answer_1 = int(input("3+3 = : "))
assert answer_1 == 6, "wrong answer"

print("correct answer")
print("next question")

answer_2 = int(input("3 + 7 = : "))
assert answer_2 == 10, "wrong answeer"

print("well done")

#Home Work
# answer_1 = int(input("3+3 = : "))
# if answer_1 == 6:
#     print("correct answer")
#     print("next question")
# else:
#     print("wrong answer")
#     print("next question")
# answer_2 = int(input("3 + 7 = : "))
# if answer_2 == 10:
#     print("well done")
# else:
#     print("wrong answer")