#Вкладені цикли range. for i in
# sequence_1 = range(5)
# print(sequence_1, type(sequence_1)) #range(0, 5) <class 'range'>
#
# for i in sequence_1:
#     print(i)
#
# new_list = list(range(5))
# print(new_list, type(new_list)) #[0, 1, 2, 3, 4] <class 'list'>

# for i in range(5, 7):
#     print(i)

# for i in range(1, 10, 3):
#     print(i)

# for i in range(5):
#     print(i) #виконається спочатку одне значення з верхнього циклу, потім повністю нижній цикл.
#     for j in range(10, 15):
#         print(j)

#Таблиця множення
# for i in range(2, 10):
#     print(f"=={i}==")
#     for j in range(2, 10):
#         print(f"{i}*{j}={i*j}")

#HW task_1 Напишіть програму на Python, яка виводить таблицю множення від 1 до 10 за допомогою вкладених циклів.
# for i in range(1, 10):
#     print(f"=={i}==")
#     for j in range(1, 10):
#         print(f"{i}*{j}={i*j}")
#HW task_2 Створіть програму, яка приймає список чисел зроблений за допомогою range. Виведіть кожне число, зведене в квадрат, за допомогою вкладеного циклу.
# for i in range(2, 9):
#     print(f"=={i}==")
#     print(f"{i}**2={i**2}")
#HW task_3 Напишіть програму, яка обчислює суму всіх чисел від 1 до 100 за допомогою циклу та функції range()
# i = list(range(1, 101))
# total_sum = sum(i)
# print(f"Сума всіх чисел від 1 до 100: {total_sum}") #Сума всіх чисел від 1 до 100: 5050
