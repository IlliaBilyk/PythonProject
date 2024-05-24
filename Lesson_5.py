#list.індексація та методи

# list_empty = []
# print(list_empty, type(list_empty))

# list_a = [12, "hello", 34.0, True, [23, 789]]
# print(list_a[0])
# print(list_a[3])
# print(list_a[4][1])
#
# print(list_a)
# list_a[0] = 200
# print(list_a)

#start program
list_items_str = input("type a list of products: ")
list_items = list_items_str.split(" ")
print(list_items, type(list_items))

del_item = input("the product you bought : ")
list_items.remove(del_item)
print(list_items)

del_item = int(input("number of product you bought : "))
list_items.pop(del_item-1)
print(list_items)

del_item = int(input("number of product you bought : "))
list_items.pop(del_item-1)
print(list_items)

del_item = int(input("number of product you bought : "))
list_items.pop(del_item-1)
print(list_items)

del_item = int(input("number of product you bought : "))
list_items.pop(del_item-1)
print(list_items)

list_amount = len(list_items)
if list_amount == 0:
    print("you bought all what you want")
else:
    print("you cart not empty")
    print(list_items)

print("if you want to add somthing please type it: ")
new_items = input("type your product")
new_items = new_items.split()
list_items.append(new_items)
print("your new list")
print(list_items)

#SUM example
# list_of_grades = [11, 12, 10, 8, 10]
# print(sum(list_of_grades))