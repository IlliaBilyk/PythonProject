#Форматування рядків
name = "Guido"
age = 67

concatenate_string = "Hi, my name is " + name + ". I am " +str(age) + " years old"
print(concatenate_string)

f_string = f"Hi, my name is {name}. I am {age} years old"
print(f_string)

assert concatenate_string == f_string

print(f"Hi, my name is {name.upper()}. I am {age + 10} years old")

format_string = "Hi, my name is {}. I am {} years old".format(name, 67)
print(format_string)
assert format_string == f_string

#Homework
#1 Напишіть програму, яка виводить на екран повідомлення про температуру зараз, якщо відомо місце проживання і температура у градусах Цельсія. Виведіть це у форматі "У місті [місце] зараз [температура] градусів Цельсія".
city = "Kryvyi Rih"
temperature = 25

answer_1 = f"In {city}, now we have {temperature} degrees Celsius"
print(answer_1)

#2 Напишіть програму, яка приймає від користувача три рядки: ім'я, вік і місце проживання. Виведіть ці дані у вигляді:
# Ім'я: [ім'я користувача]
# Вік: [вік користувача] років
# Місце проживання: [місце проживання користувача]
name = "Illia"
age = 28
location = "Kryvyi Rih, Ukraine"

answer_2 = (f"Name: {name} "
            f"Age: {age} years"
            f"Location: {location}")
print(answer_2)
#3 Напишіть програму, яка приймає від користувача довжину сторін прямокутника та обчислює його периметр і площу. Виведіть результат у такому форматі:
# Довжина: [довжина сторони]
# Ширина: [ширина сторони]
# Периметр: [значення периметра]
# Площа: [значення площі]

a = 10
b = 5
P = a + b
S = a * b

answer_3 = (f"Large: {a} "
            f"Height: {b} "
            f"Perimeter: {P} "
            f"Area: {S}")
print(answer_3)
