class Player:

    def __init__(self, name, major):
        self.name = name
        self.major = major

        self.grades = 50
        self.health = 80
        self.money = 500
        self.happiness = 70
        self.stress = 30
        self.gpa=2.5


        self.inventory = []
        self.achievements = []
        self.friends=0


    def show_stats(self):
        print("\n" + "=" * 35)
        print(f"Student: {self.name}")
        print(f"Major: {self.major}")
        print(f"Grades: {self.grades}")
        print(f"GPA: {self.gpa:.2f}")

        print(f"Health: {self.health}")
        print(f"Money: {self.money}")
        print(f"Happiness: {self.happiness}")
        print(f"Stress: {self.stress}")
        print(f"Inventory: {self.inventory}")
        print(f"Friends: {self.friends}")


        print("=" * 40)


    def study(self):
        self.grades += 10
        self.health -= 5
        self.happiness -= 5
        self.stress += 10

    def work(self):
        self.money += 150
        self.health -= 10
        self.happiness -= 5
        self.stress += 5

    def rest(self):
        self.health += 15
        self.happiness += 10
        self.stress = max(0, self.stress - 15)

    def hangout(self):
        self.happiness += 15
        self.friends += 1

        self.money -= 50
        self.stress = max(0, self.stress - 10)

    def shop(self):
        print("\n===== CAMPUS SHOP =====")
        print("1. Coffee ($50)")
        print("2. Notes ($100)")
        print("3. Gym Membership ($200)")
        print("4. Laptop Upgrade ($300)")

        choice = input("Choose item: ")

        if choice == "1" and self.money >= 50:
            self.money -= 50
            self.inventory.append("Coffee")
            self.stress=max(0,self.stress-10)
        elif choice == "2" and self.money >= 100:
            self.money -= 100
            self.inventory.append("Notes")
            self.grades += 5
        elif choice == "3" and self.money >= 200:
            self.money -= 200
            self.inventory.append("Gym Membership")
            self.health += 10
        elif choice == "4" and self.money >= 300:
            self.money -= 300
            self.inventory.append("Laptop Upgrade")
            self.grades += 10
        else:
            print("Not enough money or invalid choice.")
