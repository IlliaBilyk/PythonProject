# Кортеж tuple()
my_tuple_1 = (1, 2, 3)
print(type(my_tuple_1), my_tuple_1)

my_tuple_2 = 1, 2, 3
print(type(my_tuple_2), my_tuple_2)

my_tuple_3 = tuple([1, 2, 3])
print(type(my_tuple_3), my_tuple_3)

print(my_tuple_1[0])
print(my_tuple_1[2])

print(len(my_tuple_1))

print(1 in my_tuple_1)
print(123 in my_tuple_1)

print(11 not in my_tuple_1)

my_tuple_4 = 7, 3, 5
print(my_tuple_1 + my_tuple_4)
print(my_tuple_4 + my_tuple_1)

for i in my_tuple_4:
    print(i)

print(min(my_tuple_4))
print(max(my_tuple_4))
print(sum(my_tuple_4))

print(my_tuple_4.index(7))
print(my_tuple_4.count(3))