# 1. მოცემულია სია:
#
# (სახელი, გვარი, ასაკი)
#
#
# დაწერეთ უსასრულო ციკლი, რომელშიც მომხმარებელს ჰკითხავთ სახელს, თუ სახელი იქნება მოცემულ სიაში, შემდეგ ჰკითხეთ გვარი და გვარიც თუ იქნება,
# დაბეჭდეთ მისი ასაკი, ხოლო თუ არ იქნება სახელი დაბეჭდეთ რომ არ არის მოცემული სახელი, შესაბამისად გვარი აღარ ჰკითხოთ, ანალოგიურად
# მოიქეცით გვარის კითხვის შემთხვევაშიც. ციკლი უნდა გაჩერდეს იმ შემთხვევაში თუ მომხმარებელი შემოიყვანს სიტყვას "stop".

persons = [
    ('Kelly', 'Simpson', 26),
    ('Erika', 'Stephens', 24),
    ('Cheryl', 'Dunn', 30),
    ('Amy', 'Larsen', 49),
    ('Christine', 'Gordon', 23),
    ('Monica', 'Huff', 38),
    ('David', 'Nixon', 36),
    ('Cindy', 'Escobar', 41),
    ('Cindy', 'White', 33),
    ('Joel', 'Hall', 43),
    ('Steven', 'Winters', 28),
    ('Alex', 'Cole', 68),
    ('Alex', 'Smith', 32),
    ('Brittany', 'Thompson', 18),
    ('Ernest', 'Young', 43),
    ('Traci', 'Wells', 38),
    ('Andrew', 'Flores', 61),
    ('Christopher', 'Lewis', 29),
    ('Kevin', 'Willis', 57),
    ('Kayla', 'Lucas', 28),
    ('Michelle', 'Rush', 43),
    ('Thomas', 'Mason', 37)
]



while True:
    found_name = False
    found_surname = False
    user_name = input("Please enter name(enter 'stop' to quit): ")
    if user_name == 'stop':
        break
    for item in persons:
        if item[0] == user_name.capitalize():
            found_name = True
            user_surname = input('Please enter surname: ')
            while True:
                for item in persons:
                    if item[0] == user_name.capitalize() and item[1] == user_surname.capitalize():
                        print(f'{item[0]} {item[1]} is {item[2]} years old.')
                        found_surname = True
                        break
                    else:
                        pass
                break

            if found_surname == False:
                print("no such surname")
            break

    if found_name == True and found_surname == True:
        pass
    elif found_name == True and found_surname == False:
        pass
    elif found_name == False:
        print("no such name")







