# 2. დაწერეთ ფუნქცია რომელიც მიიღებს არგუმენტების განუსაზღვრელ რაოდენობას მთელი რიცხვების სახით და დააბრუნებს
#    ორ ლისტს, ერთ ლისტში იქნება გადაცმული არგუმენტებიდან კენტი რიცხვები ხოლო მეორე ლისტში ლუწი რიცხვები


def even_or_odd(*args):
    even_lst = []
    odd_lst = []
    for item in args:
        if item % 2 == 0:
            even_lst.append(item)
        else:
            odd_lst.append(item)

    return even_lst, odd_lst


print(even_or_odd(1,2,3,30,4,5,6,7,52,23,77,100,8,9,10))