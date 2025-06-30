# 1. შექმენით მთელი რიცხვების მინიმუმ 5 ელემენტიანი სია, გამოთვალეთ ყველა რიცხვის ჯამი და საშუალო, არ გამოიყენოთ ჩაშენებული ფუნქციები!


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 25]
sum = 0


for i in my_list:
    sum += i

average = sum / len(my_list)

print(f'The sum is: {sum} and the average is: {average}')