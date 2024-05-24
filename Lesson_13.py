#Цілочисельне діленняю Остача від ділення

total_adds = 92
adds_per_pages = 8
full_pages_count = total_adds // adds_per_pages
print(full_pages_count) #11
last_page_adds = total_adds % adds_per_pages
print(last_page_adds) #4

total_apples = 11
total_people = 3
apple_per_person = total_apples // total_people
print(apple_per_person) #3
last_apples = total_apples % total_people
print(last_apples) #2