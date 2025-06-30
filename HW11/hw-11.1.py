# 1. დაწერეთ პროგრამა, რომელიც მომხმარებელს უსასრულოდ შეეკითხება ჯერ სახელს, შემდეგ გვარს და რაიმე ფაილში ჩაწერს
#    სახელს და გვარს ერთ ხაზზე თავისი ნუმერაციით, ყველა ახალი სახელი და გვარი უნდა იყოს ახალ ხაზზე ჩაწერილი, მაგალითად:
#
#    Enter your first name: Otar
#    Enter your last name: Tumanishvili
#    Enter your first name: Nika
#    Enter your last name: Papaskiri
#    Enter your first name: stop
#
#    ფაილში უნდა ჩაიწეროს შემდეგი სახით:
#    1. Otar Tumanishvili
#    2. Nika Papaskiri

def names():
    line = 1
    file = open("hw-11.1.txt", 'w')
    while True:
        first_name = input('Enter your first name: ')
        if first_name == 'stop':
            file.close()
            break
        last_name = input('Enter your last name: ')
        file.writelines(str(line) + '. ' + first_name + ' ' + last_name + '\n')
        line += 1




names()
