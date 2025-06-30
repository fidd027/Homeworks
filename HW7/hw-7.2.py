# 2. დაწერეთ პროგრამა, რომელიც მომხმარებელს შემოაყვანინებს ჯერ პირველ და მერე მეორე სიტყვას.
#    იპოვეთ ამ სიტყვებში საერთო სიმბოლოები, განსხვავებული სიმბოლოები, და გაერთიანებული სიმბოლოები(ანუ ორივეში ერთად რომელიცაა ყველა ერთად)
#    დაბეჭდეთ ყველა ზემოთჩამოთვლილი(გამოიყენეთ set)


word1 = input('Enter the first word: ')
word2 = input('Enter the second word: ')

set1 = set(list(word1))
set2 = set(list(word2))



saerto = set1.intersection(set2)
print(f"am sityvebshi saerto asoebia: {saerto}")

gansxvavebuli = set1.symmetric_difference(set2)
print(f"am sityvebhi gansxvavebuli asoebia: {gansxvavebuli}")

gaertianebuli = set1.union(set2)
print(f'am sityvebshi gaertianebuli asoebia: {gaertianebuli}')