# 2. მოცემულია სია ['a', 'b', 2, 4, 2, 'c', 'j', 1, 'b', 'd', 'c', 4, 1], დაწერეთ ლოგიკა, როემლიც ამ ლისტში დატოვებს უნიკალურ
# ელემენტებს, ანუ არ განმეორდება ელემენტები. არ გამოიყენოთ set!


my_list = ['a', 'b', 2, 4, 2, 'c', 'j', 1, 'b', 'd', 'c', 4, 1]
new_list = []

for item in my_list:
    if item not in new_list:
        new_list.append(item)


my_list = new_list
print(my_list)










