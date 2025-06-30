# 1. დაწერეთ ფუნქცია, რომელიც ატრიბუტად მიიღებს რიცხვს, რა რიცხვსაც გადავცემთ, იმდენჯერ შეეკითხება მომხმარებელს
#    სახელს, გვარს და ასაკს. ანუ თუ გადავეცით 3, 3-ჯერ შეეკითხება მომხმარებელს აღნიშნულ ინფორმაციას, ინფუთის
#    საფუძველზე csv ფაილში ჩაწერეთ შესაბამისი ინფორმაცია შემდეგი სახით, მაგალითად:
#
#    ID,first_name,last_name,age
#    1,John,Doe,25
#    2,Alice,White,30
#
#    და ა.შ.
#
#    გამოიყენეთ try, ecxept იმისათვის რომ მომხმარებელმა ასაკის შემოყვანის დროს აუცილებლად ინტეჯერი შემოიყვანოს!
#    ფაილში ჩასაწერად აუცილებლად გამოიყენეთ csv მოდულიდან writer და DictWriter!
import csv

def function(k):
    iteration = 1
    with open("info.csv", 'w', newline='') as csvfile:
        header = ['ID', 'first_name', 'last_name', 'age']
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()

        while iteration <= k:
            name = input("Enter a name: ")
            surname = input("Enter a surname: ")
            # ქვემოთ მოცემული კოდი იმისთვის დავწერე, რომ მიუხედავად try except ბლოკისა, თუ პირველ იტერაციაზე, როცა age-s არ ჰქონდა მნიშვნელობა
            # მომხმარებელი სწორად არ შემოიყვანდა ინპუტს, ასაკის არ ქონის ქამო ქვევით 38-ე ხაზზე ვრაითროუ აერორებდა.
            # ამ კოდით კი მომხმარებელს იქამდე შეეკითხება ასაკს, სანამ სწორი ფორმატით არ შემოიყვანს

            while True:
                age = ' '
                try:
                    age = int(input("Enter age: "))
                except ValueError as err:
                    print(err)
                if type(age) is int:
                    break

            writer.writerow({'ID': iteration, 'first_name': name, 'last_name': surname, 'age': age})
            iteration += 1



        
function(3)

