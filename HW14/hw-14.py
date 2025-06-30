# შექმენით Student კლასი
# კლასს უნდა გააჩნდეს შემდეგი ატრიბუტები:
# status, ნაგულისხმევად უნდა იყოს True
# pay რომელიც იქნება 1000
#
# არსებული კლასის ინსტანსს უნდა გააჩნდეს შემდეგი ატრიბუტები:
# first_name(ტექსტური), last_name(ტექსტური), age(ინტეჯერი), grades(სია, რომელშიც რამდენიმე ქულა იქნება)
#
# დაუმატეთ შემდეგი მეთოდები:
# get_full_name - რომელიც დააბრუნებს სახელს(first_name) და გვარს(last_name) ერთად, სფეისით დაშორებულს
# get_discount - თუ ინსტანსის ასაკი იქნება 18 წელზე ნაკლები, გადასახადი(pay) შემცირდეს 20%-ით
# calculate_average - დააბრუნებს საშუალო ქულას grades სიაზე დაყრდნობით
# get_status - თუ საშუალო ქულა(calculate_average) მეტი იქნება 90-ზე, დააბრუნებს "Excellent", თუ 90-სა და 70-ს შორის არის,
# დააბრუნებს "Good", თუ 70-სა და 50-ს შორის დააბრუნებს "Average", ხოლო 50ზე ნაკლები თუა, დააბრუნებს "Poor" და status
# ატრიბუტიც უნდა შეიცვალოს და გახდეს False
#
#
#

class Student:
    status = True
    pay = 1000

    def __init__(self, first_name, last_name, age, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.age = int(age)
        self.grades = list(grades)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_discount(self):
        if self.age < 18:
            self.pay *= 0.8
        else:
            pass
        return 'Discound applied if all conditions are met.'

    def calculate_average(self):
        return sum(self.grades) / len(self.grades)

    def get_status(self):
        if self.calculate_average() > 90:
            return "Excellent"
        elif 70 < self.calculate_average() <= 90:
            return "Good"
        elif 50 < self.calculate_average() <= 70:
            return "Average"
        else:
            self.status = False
            return "Poor"


stud1 = Student('Pridoni', 'Bagashvili', 25, [100, 85, 95, 82])
stud2 = Student('Mariam', 'Bagashvili', 17, [50, 70, 75, 80])
stud3 = Student('Levan', 'Titvelashvili', 24, [25, 60, 45, 34])

print(stud1.get_full_name(), stud1.get_discount(), stud1.calculate_average(), stud1.get_status())

print(stud2.get_full_name(), stud2.get_discount(), stud2.calculate_average(), stud2.get_status())

print(stud3.get_full_name(), stud3.get_discount(), stud3.calculate_average(), stud3.get_status())





