# 3. დააგენერირეთ 20 ელემენტიანი რიცხვების სია, რომელიც შევსებული იქნება -50 დან 50-მდე შემთხვევითი რიცხვებით და შექმენით მეორე
# სია, რომელიც პირველი სიიდან იქნება შევსებული მხოლოდ ლუწი რიცხვებით და დაბეჭდეთ ორივე სია, გამოიყენეთ აუცილებლად ლისტის გენერატორი!



import random


# for i in range(20):   ეს სტანდარტული ჩანაწერი, ქვევით კი ლისტ ქომფერჰენშენი
#     my_list.append(random.randint(-50,50))

my_list = [random.randint(-50,50) for i in range(20)]

# even_num_list = []
#
# for i in my_list:
#     if i % 2 == 0:
#         even_num_list.append(i)

even_num_list = [i for i in my_list if i % 2 == 0]

print(f"this is random num list: {my_list}  ")
print(f'and this is list of even numbers from the original one: {even_num_list}')