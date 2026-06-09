class Player:

    def __init__(self, name, major):
        self.name = name
        self.major = major

        self.grades = 50
        self.health = 80
        self.money = 500
        self.happiness = 70

        self.inventory = []
        self.achievements = []

    def show_stats(self):
        print("\n==============================")
        print(f"Student: {self.name}")
        print(f"Major: {self.major}")
        print(f"Grades: {self.grades}")
        print(f"Health: {self.health}")
        print(f"Money: {self.money}")
        print(f"Happiness: {self.happiness}")
        print("==============================")

    def study(self):
        self.grades += 10
        self.health -= 5
        self.happiness -= 5

    def work(self):
        self.money += 150
        self.health -= 10
        self.happiness -= 5

    def rest(self):
        self.health += 15
        self.happiness += 10

    def hangout(self):
        self.happiness += 15
        self.money -= 50