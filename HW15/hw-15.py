# Football Team Managmenet System
#
# შექმენით კლასი FootballTeam შემდეგი ატრიბუტებით:
# team_name (string) - კლუბის სახელი
# coach (string) - მწვრთნელი
# players - მოთამაშეების სია(შექმნისას ცარიელი უნდა იყოს)
#
# კლასს უნდა გააჩნდეს შემდეგი მეთოდები:
# 1. მოთამაშის დამატება - მოთამაშის სახელი, პოზიცია, სათამაშო ნომერი,
#    ასაკი და ეროვნება(დიქტის სახით უნდა დაემატოს მოთამაშეების სიაში)
#
# 2. მოთამაშის წაშლა - მოთამაშე უნდა წაიშალოს სიიდან სათამაშო ნომრის მიხედვით
#
# 3. მოთამაშის ინფორმაციის განახლება - მოთამაშე უნდა მონახოთ სათამაშო ნომრის მიხედვით
#    და უნდა დაუსეტოთ ისეთი ინფორმაცია, რომელსაც გადასცემთ ამ მეთოდს, მაგ: "goal": 1
#    ანუ key და value უნდა იყოს გადაცემული ამავე მეთოდის გამოძახებისას!
#
# 4. კლუბის ინფორმაციის ჩვენება - გამოიტანეთ კლუბის სახელი, მწვრთნელის სახელი და მოთამაშეების სია
#
# 5. მოთამაშის ინფორმაციის ჩვენება - უნდა გამოიტანოთ ინფორმაცია მოთამაშის ნომრის მიხედვით


class FootballTeam:
    team_name = "Tigers"
    coach = "Pridoni Bagashvili"
    players = []

    def __init__(self, team_name, coach):
        self.team_name = team_name
        self.coach = coach

    @staticmethod
    def add_player(name, position, number, age, nationality):
        player = {"name": name,
                  "position": position,
                  "number": number,
                  "age": age,
                  "nationality": nationality}
        FootballTeam.players.append(player)

    def remove_player(self, number):
        for player in self.players:
            if player["number"] == number:
                self.players.remove(player)
                print(f"removed player with number {number}")
                return
        print(f"player with number {number} not found")

    def player_update(self, number, key, value):
        for player in self.players:
            if player["number"] == number:
                player[key] = value

    def get_player(self, number):
        for player in self.players:
            if player["number"] == number:
                return print(player)



    def get_club_info(self):
        print(f"Club: {self.team_name}")
        print(f"Coach: {self.coach}")
        print("List of Players:")
        for i in self.players:
            print(i)

# მეთოდი 1
team = FootballTeam("Tigers", "Pridoni Bagashvili")
team.add_player("fido", "Forward", 27, 25, "Georgia")
team.add_player("daviti", "Striker", 11, 28, "Georgia")
team.add_player("Cristiano", "Left Wing", 7, 41, "Portugal")


# მეთოდი 4- კლუბის ინფოს ჩვენება
team.get_club_info()

# მეთოდი 2- წაშლა ნომრის მიხედვით
team.remove_player(27)

# მეთოდი 3 - მოთამაშის ინფოს განახლება
team.player_update(7, "age", 30)


team.get_club_info()
# მეთოდი 5- მოთამაშის ინფოს გამოტანა ნომრის მიხედვით
team.get_player(11)
