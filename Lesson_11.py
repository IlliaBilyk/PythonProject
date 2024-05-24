#Зрізи списків та рядків

list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list_a[0]) #1
print(list_a[-1]) #10
print(list_a[:6]) #[1, 2, 3, 4, 5, 6]
print(list_a[6:]) #[7, 8, 9, 10]
new_list = list_a[:6]
print(list_a)
print(new_list)
message = "don't subscribe"
print(message[:6]) #don't
print(message[:6].upper()) #DON'T
print(list_a[-5:-2]) #[6, 7, 8]
print(list_a[-1:-2]) #[]
print(list_a[::3]) #[1, 4, 7, 10]
print(list_a[::-3]) #[10, 7, 4, 1]
print(list_a[8:2:-1]) #[9, 8, 7, 6, 5, 4]