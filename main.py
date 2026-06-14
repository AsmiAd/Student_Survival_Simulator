from dashboard import show_dashboard
from player import Player
from events import random_event
from achievements import check_achievements
from data import MAJORS
import player

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

        print("\n1. Study (+10 Grades, -5 Health, -5 Happiness, +10 Stress)")
        print("2. Part-Time Job (+150 Money, -10 Health, -5 Happiness, +5 Stress)")
        print("3. Rest (+15 Health, +10 Happiness, -15 Stress)")
        print("4. Hang Out (+15 Happiness, +1 Friend, -50 Money, -10 Stress)")
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

    print('\n========== SEMESTER REPORT ==========' )
    p.show_stats()
    show_dashboard(p, week)

    if p.grades>=90 and p.health>=80 and p.happiness>=80:
        print("\n🌟 LEGENDARY STUDENT ENDING 🌟")
    elif p.grades>=90:
        print("\n🏅 HONORS STUDENT ENDING")
    elif p.grades>=60:
        print("\n🎓 SUCCESSFUL GRADUATION")
    else:
        print("\n😭 FAILED SEMESTER")


while True:
    play_game()
    if input("\nPlay Again? (yes/no): ").lower()!="yes":
        break
