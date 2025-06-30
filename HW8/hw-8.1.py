# 1. დაწერეთ ფუნქცია, რომელიც პარამეტრად მიიღებს მომხმარებლის მიერ შეყვანილ
# ტექსტს და ამ ტექსტში დათვლის რამდენი სიმბოლო იყო მაღალ რეგისტრში
#    შეყვანილი და ასევე ამ ტექსტს გადააქცევს uppercase-ად ანუ მაღალ რეგისტრში დააბრუნებს, მაგალითად, მომხმარებელმა თუ შეიყვანა ტექსტი
#    Hello woRld, ფუნქციამ უნდა დააბრუნოს რომ 2 დიდი ამ ტექსტში და ეს ტექსტი აქციოს HELLO WORLD-ად.


def text_function(p1):
    upper_counter = 0
    for letter in p1:
        if letter.isupper():
            upper_counter += 1

    return print(f"There are {upper_counter} upper case letters and the text itself is: {p1.upper()}")


user_text = input("Please input any text: ")
text_function(user_text)
#აქ ფუნქციის გამოძახებისას პრინტში იმიტო აღარ ჩავსვი რო რეთარნში ისედაც პრინტი
# გვქონდა და ჩვენთვის სასურველ ტექსტთან ერთად none საც დააბრუნებდა