# 2. დაწერეთ პროგრამა, რომელიც მომხმარებლის მიერ შემოყვანილ წინადადებაში იპოვის ყველაზე
# გრძელ სიტყვას და დაბეჭდავს მას. არ გამოიყენოთ max() ფუნქცია!

sentence = input("please input any completed sentence that you like: ")

sentence_split = sentence.split(" ")
longest_word = ""
for i in sentence_split:
    if len(i) > len(longest_word):
        longest_word = i

print('Longest word in the sentence is: ', longest_word)