class Player:
    def __init__(self, name, major):
        self.name=name
        self.major=major
        self.grades=50
        self.health=80
        self.money=500
        self.happiness=70
        self.stress=30
        self.gpa=2.5
        self.inventory=[]
        self.achievements=[]
        self.friends=0

    def show_stats(self):
        print("\n"+"="*40)
        print(f"Student: {self.name}")
        print(f"Major: {self.major}")
        print(f"GPA: {self.gpa:.2f}")
        print(f"Grades: {self.grades}")
        print(f"Health: {self.health}")
        print(f"Money: {self.money}")
        print(f"Happiness: {self.happiness}")
        print(f"Stress: {self.stress}")
        print(f"Friends: {self.friends}")
        print(f"Inventory: {self.inventory}")
        print("="*40)

    def study(self):
        print("\n📚 You spent the week studying hard.")
        print("Grades +10 | Health -5 | Happiness -5 | Stress +10")
        self.grades+=10; self.health-=5; self.happiness-=5; self.stress+=10

    def work(self):
        print("\n💼 You worked a part-time job.")
        print("Money +150 | Health -10 | Happiness -5 | Stress +5")
        self.money+=150; self.health-=10; self.happiness-=5; self.stress+=5

    def rest(self):
        print("\n😴 You took time to recover.")
        print("Health +15 | Happiness +10 | Stress -15")
        self.health+=15; self.happiness+=10; self.stress=max(0,self.stress-15)

    def hangout(self):
        print("\n🎉 You hung out with friends.")
        print("Happiness +15 | Friends +1 | Money -50 | Stress -10")
        self.happiness+=15; self.friends+=1; self.money-=50; self.stress=max(0,self.stress-10)

    def shop(self):
        print("\n===== CAMPUS SHOP =====")
        print("1. Coffee ($50) -> Stress -10")
        print("2. Notes ($100) -> Grades +5")
        print("3. Gym Membership ($200) -> Health +10")
        print("4. Laptop Upgrade ($300) -> Grades +10")
        choice=input("Choose item: ")
        if choice=="1" and self.money>=50:
            self.money-=50; self.inventory.append("Coffee"); self.stress=max(0,self.stress-10)
            print("☕ Coffee purchased! Stress -10")
        elif choice=="2" and self.money>=100:
            self.money-=100; self.inventory.append("Notes"); self.grades+=5
            print("📒 Notes purchased! Grades +5")
        elif choice=="3" and self.money>=200:
            self.money-=200; self.inventory.append("Gym Membership"); self.health+=10
            print("🏋️ Gym Membership purchased! Health +10")
        elif choice=="4" and self.money>=300:
            self.money-=300; self.inventory.append("Laptop Upgrade"); self.grades+=10
            print("💻 Laptop Upgrade purchased! Grades +10")
        else:
            print("Not enough money or invalid choice.")
