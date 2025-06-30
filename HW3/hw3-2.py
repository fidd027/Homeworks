# 2. დაწერეთ პროგრამა, რომელიც მომხმარებელს შეეკითხება რიცხვს და გამოითვლის არ რიცხვის ფაქტორიალს,
# შეგახსენებთ რომ ფაქტორიალი
# არის ამ რიცხვის ნამრავლი ყველა მთელ რიცხვზე 1-მდე, ანუ 5-ის
# ფაქტორიალი არის 5 X 4 X 3 X 2 X 1 (დაწერეთ for ლუპის გამოყენებით)


usr_input = int(input("please insert a natural number(exm: 7; 9;) "))
final_number = 1
for i in range(1, usr_input + 1):
    final_number *= i
print(final_number)