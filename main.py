
from player import Player
from events import random_event
from achievements import check_achievements
from data import MAJORS
import matplotlib.pyplot as plt

def show_graphs(player):
    weeks = range(1, len(player.grades_history)+1)

    plt.figure(figsize=(8,5))
    plt.plot(weeks, player.grades_history, label="Grades")
    plt.plot(weeks, player.health_history, label="Health")
    plt.plot(weeks, player.money_history, label="Money")
    plt.plot(weeks, player.stress_history, label="Stress")
    plt.title("Student Journey Through The Semester")
    plt.xlabel("Week")
    plt.ylabel("Value")
    plt.legend()
    plt.grid(True)
    plt.show()

def play_game():
    print("="*50)
    print("🎓 STUDENT SURVIVAL SIMULATOR DELUXE")
    print("="*50)

    name=input("Enter your name: ")

    print("\nChoose your major:")
    print("1. Computer Engineering")
    print("2. Business")
    print("3. Medicine")
    major=MAJORS.get(input("Choice: "), "Computer Engineering")

    p=Player(name,major)

    print("\nChoose Difficulty")
    print("1. Easy")
    print("2. Normal")
    print("3. Hard")

    diff=input("Choice: ")

    if diff=="1":
        p.money=700; p.health=100; p.stress=10
    elif diff=="3":
        p.money=300; p.health=60; p.stress=50

    housing=input("Housing (Hostel/Apartment/Family): ")
    if housing.lower()=="family":
        p.money+=100
    elif housing.lower()=="hostel":
        p.friends+=1

    for week in range(1,13):
        print(f"\n========== WEEK {week} ==========")
        p.show_stats()

        if week==6:
            print("\n📚 MIDTERM EXAMS")
            if p.grades>=70:
                p.grades+=10
            elif p.grades>=50:
                p.grades+=5
            else:
                p.grades-=10

        if week==8:
            print("\n💼 Internship Opportunity!")
            if input("Apply? (yes/no): ").lower()=="yes":
                if p.grades>=70:
                    p.money+=300
                    p.happiness+=10
                    print("Internship secured!")
                else:
                    print("Application rejected.")

        print("\n1. Study")
        print("2. Part-Time Job")
        print("3. Rest")
        print("4. Hang Out")
        print("5. Campus Shop")

        action=input("Choose: ")

        if action=="1":
            p.study()
        elif action=="2":
            p.work()
        elif action=="3":
            p.rest()
        elif action=="4":
            p.hangout()
        elif action=="5":
            p.shop()

        random_event(p)
        check_achievements(p)

        p.record_week()

        if p.health<=0 or p.stress>=150:
            print("\n😫 BURNOUT ENDING")
            return
        if p.money<=0:
            print("\n💸 FINANCIAL CRISIS ENDING")
            return

    print("\n📝 FINAL EXAMS")
    if p.grades>=80:
        p.grades+=15
    elif p.grades>=60:
        p.grades+=5
    else:
        p.grades-=10

    p.gpa=max(0,min(4.0,p.grades/25))

    resume_score = p.grades + (p.money//10) + (p.friends*5)

    print(f"\nResume Score: {resume_score}")

    if resume_score>=150:
        print("🏆 Dream Job Achieved!")
    elif resume_score>=100:
        print("🎉 Good Career Start!")
    else:
        print("📈 Needs Improvement!")

    p.show_stats()

    if p.grades>=90 and p.health>=80 and p.happiness>=80:
        print("\n🌟 LEGENDARY STUDENT ENDING 🌟")
    elif p.grades>=90:
        print("\n🏅 HONORS STUDENT ENDING")
    elif p.grades>=60:
        print("\n🎓 SUCCESSFUL GRADUATION")
    else:
        print("\n😭 FAILED SEMESTER")

    show_graphs(p)

while True:
    play_game()
    if input("\nPlay Again? (yes/no): ").lower()!="yes":
        break
