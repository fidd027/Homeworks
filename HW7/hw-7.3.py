# 3. დაწერეთ პროგრამა, რომელიც მომხმარებელს შემოაყვანინებს წინადადებას და ამ წინადადების თითოეულ სიმბოლოს დააბრუნებს
# ტაპლის სახით, მაგალითად "I love python" უნდა გადააქციოს შემდეგი სახით:
# ('I', 'l', 'o', 'v', 'e', 'p', 'y', 't', 'h', 'o', 'n').
# გაითვალისწინეთ რომ ტაპლში არ უნდა იყოს ცარიელი ადგილები!

sentence = input("please enter any sentence: ")
l1 = []
for letter in sentence:
    if letter == ' ':
        pass
    else:
        l1.append(letter)

final_tuple = tuple(l1)
print(final_tuple)

