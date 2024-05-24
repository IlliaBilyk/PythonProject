#Словники. Варіанти створення.

# my_list = [10, [99, 109, 1], "hello"]
# print("===list value====")
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])

# my_dict = {"first_key":"first_value", 777:[34, 1000], (45, 1): 4324}
# print(my_dict["first_key"])
# print(my_dict[777])
# print(my_dict[(45, 1)])

# dict_1 = {"first_key": "first_value", "second_key": "second_value"}
# print(type(dict_1))
# print(dict_1)

# dict_2 = dict([["first_key", "first_value"], ["second_key", "second_value"]])
# print(type(dict_2))
# print(dict_2)

# dict_3 = dict.fromkeys(["key_1", "key_2", "key_3"], "values")
# print(type(dict_3))
# print(dict_3)

#HW task_1 Напишіть програму, що створює словник для конвертації валют, де ключами є валютні коди (наприклад, USD, EUR), а значеннями - курс обміну до гривні.
# dict_1 = {"USD": 40, "EUR": 42}
# print(dict_1)

#HW task_2 Уявімо, що ми маємо список предметів, і нам потрібно створити словник, де кожен предмет буде ключем, а початкове значення для кожного ключа буде встановлене як певна оцінка (наприклад, 0).
# dict_2 = {"Math": 2, "Physics": 4, "Biology": 3, "History": 5}
# print(dict_2)
# subjects = ["Math", "Physics", "Biology", "History"]
# dict_2 = dict.fromkeys(subjects, 0)
# print(dict_2)

#HW task_3 Напишіть програму для створення словника, де ключами будуть імена студентів, а значеннями - їхні середні бали
# dict_3 = {"Jhon": 4.2, "Mary": 5.0, "Steven": 4.68, "Mark": 3.79}
# print(dict_3)