# 3. დაწერეთ პროგრამა, რომელიც მომხმარებელს შეეკითხება ხილის სახელს, მანამ სანამ, მომხმარებელი არ შეიყვანს სიტყვას stop,
#    ამის შემდეგ გამოიტანეთ დიქტის სახით ხილის დასახელება და ველიუ იქნება რამდენჯერაც შეიყვანა ეს ხილი, მაგალითად:
#
#    Enter your favorite fruit: banana
#    Enter your favorite fruit: apple
#    Enter your favorite fruit: banana
#    Enter your favorite fruit: stop
#
# შედეგი:
#
# {'banana': 2, 'apple': 1}

user_input = ''
user_dict = {}
while True:
    user_input = input('Enter your favorite fruit: ')
    if user_input.lower() == 'stop':
        break
    if user_input.lower() not in user_dict.keys():
        user_dict.update({user_input: 1})
    else:
        user_dict.update({user_input.lower(): user_dict[user_input.lower()] + 1})


print(user_dict)
