# 3. დაწერეთ პროგრამა, რომელიც მომხმარებელს შეეკითხება ორ სიტყვას შეამოწმებს არის თუ არა ერთმანეთის ანაგრამა
# ანაგრამა არის ერთ სიტყვაში ასოების გადაადგილებით მიღებული მეორე სიტყვა, მაგალითად ("listen", "silent" ), ("Triangle", "Integral")
# და ა.შ. უნდა იყოს case-insensitive, ანუ მომხმარებელი დიდი ასოებით შემოიყვანს თუ არა ტექსტს, არ უნდა ჰქონდეს მნიშვნელობა.
# არ გამოიყენოთ sorted() ფუნქცია.
from collections import Counter

word1 = input("please input the first word: ")
word2 = input("please input the second word: ")

if len(word1) == len(word2) and  Counter(word1.lower()) == Counter(word2.lower()):
    print('given words are anagrams')
else:
    print('given words are not anagrams')
