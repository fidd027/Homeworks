# 2. დაწერეთ ფუნქცია, რომელიც პარამეტრად მიიღებს ე.წ. camel case ცვლადებს და
# დააბრუნებს snake case სახით, ანუ თუ გადავცემთ ცვლადს
#    firstName დააბრუნებს first_name, name დააბრუნებს ისევ name,
# preferredFirstName დააბრუნებს preferred_first_name, lastName დააბრუნებს
#    last_name და ასე შემდეგ.


string = "ertiOriSami"


def transformation(p1):
    result = ""
    for char in p1:
        if char.isupper():
            result += "_" + char.lower()
        else:
            result += char
    # პირობა არ გვთხოვდა ამას მაგრამ თუ გადაცემული ტექსტი დიდი ასოთ დაიწყება, ზემოთა ბლოკიდან გამომდინარე მიღებული შედეგიც
    # დაიწყება ქვედა ტირეთი "_", ამიტომ ქვემოთა ბლოკში თუ ასეთი შემთხვევა გვექნება შედეგი დაიწყება მეორე ასოდან და პირველ ქვედა ტირეს გამოტოვებს
    if result.startswith("_"):
        result = result[1:]

    return result

print(transformation(string))


