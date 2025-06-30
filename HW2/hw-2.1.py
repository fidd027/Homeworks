# 1. დაწერეთ პროგრამა, რომელიც მომხმარებელს შეეკითხება მართკუთხა სამკუთხედის კათეტების სიგრძეს(მთელი დადებითი რიცხვი) და გამოითვლის
# ამ სამკუთხედის ჰიპოთენუზის სიგრძეს და ფართობს.


a = int(input("sheiyvanet samkutxedis pirveli katetis sigrdze "))
b = int(input("sheiyvanet samkutxedis meore katetis sigrdze "))
c = ((a**2) + (b**2)) ** (1/2)
s = (a * b) / 2

print(f'samkutxedis hipotenuza udris {c}-s, xolo misi fartobi udris {s}-s')