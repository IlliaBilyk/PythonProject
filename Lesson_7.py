#Цикл while. Як не залишитися в циклі

# counter = 0
#
# while counter < 5:
#     print(counter)
#     counter = counter + 1
#
# print("next line")

attempt = 0
pin_code = "1234"

while attempt < 3:
    your_pin = input("enter your pin: ")
    if your_pin == pin_code:
        print("your balance: 10 000")
        break
    else:
        print("wrong password")
    attempt = attempt + 1

print("have a good day")