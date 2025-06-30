# 1. დაწერეთ პროგრამა, რომელიც მომხმარებელს შემოაყვანინებს წინადადებას, პირველ სიტყვას და მეორე სიტყვას და შემოყვანილ წინადადებაში
# პირველ სიტყვას ჩაანაცვლებს მეორე სიტყვით

sentence = input("please input any completed sentence that you like: ")
word1 = input("please input a word that you want to be replaced in the sentence: ")
word2 = input("please input a word that you want to replace with in  the sentence: ")

sentence = sentence.replace(word1, word2)
print("your new sentence is:", sentence)