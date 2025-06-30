# 3. დაწერეთ ფუნქცია, რომელსაც პარამეტრად გადაეცემა მომხმარებლის მიერ შეყვანილი წინადადება და ამ წინადადებაში დაითვლის სიტყვებს
#    და დიქტის სახით დააბრუნებს თუ რომელი სიტყვა რამდენჯერ არის, მაგ: "This is a test. This test is fun." --> დააბრუნებს დიქტის
#    შემდეგი სახით: {'this': 2, 'is': 2, 'a': 1, 'test': 2, 'fun': 1} უნდა იყოს case insensitive (ანუ დიდ და პატარა ასოებს არ უნდა
#    ჰქონდეს მნიშვნელობა!)




user_sentence = input("Enter a sentence: ")

def function(sentence):
    dict1 = {}
    sentence = sentence.split()
    sentence_lower = [i.lower() for i in sentence]
    for word in sentence_lower:
        if word[-1] == ',' or word[-1] == '.':
            dict1[word[:-1]] = dict1.get(word[:-1], 0) + 1
        else:
            dict1[word] = dict1.get(word, 0) + 1

    return dict1

print(function(user_sentence))





