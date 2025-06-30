# 1. დაწერეთ პროგრამა რომელიც მომხმარებელს ჰკითხავს წონას(კგ) და სიმაღლეს(მ), შეყვანილი მონაცემების
# საფუძველზე გამოითვლის BMI-ს(Body Mass Index). ფორმულა: წონა გაყოფილი სიმაღლის კვადრატზე
# თუ BMI ნაკლებია 19-ზე, გამოიტანეთ ინფო რომ ის არის underweight
# თუ BMI არის 19 და 25 შორის, გამოიტანეთ ინფო რომ ის არის normalweight
# თუ BMI მეტია 25-ზე, გამოიტანეთ ინფო რომ ის არის overweight


weight = float(input("please input your weight: "))
height = float(input("please input your height in meters(exm: 1.75): "))

bmi = weight / (height ** 2)

if bmi < 19:
    print("you are underweight")
elif 19 <= bmi <= 25:
    print("you have normal weight")
elif bmi > 25:
    print("you are overweight")
else:
    print('you have supernatural BMI, please consult doctor :)')

