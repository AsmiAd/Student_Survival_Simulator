from player import Player
from events import random_event
from achievements import check_achievements
from data import MAJORS

def graduation(player):
    player.gpa=max(0,min(4.0,player.grades/25))

    print("\nFINAL RESULTS")
    player.show_stats()

    print("\nAchievements")
    for a in player.achievements:
        print("-",a)

    if player.grades>=90 and player.health>=80 and player.happiness>=80:
        print("\nLEGENDARY STUDENT ENDING")
    elif player.grades>=90:
        print("\nHONORS STUDENT ENDING")
    elif player.grades>=60:
        print("\nGRADUATED SUCCESSFULLY")
    else:
        print("\nFAILED SEMESTER")

def play_game():
    print("=" * 45)
    print("🎓 STUDENT SURVIVAL SIMULATOR")
    print("=" * 45)

    name = input("Enter your name: ")

    print("\nChoose your major:")
    print("1. Computer Engineering")
    print("2. Business")
    print("3. Medicine")

    choice = input("Choice: ")

    major = MAJORS.get(choice, "Computer Engineering")

    p=Player(name,major)

    housing=input("Housing (Hostel/Apartment/Family): ")
    if housing.lower()=="family":
        p.money+=100
    elif housing.lower()=="hostel":
        p.friends+=1


    for week in range(1, 13):

        print(f"\n========== WEEK {week} ==========")

        p.show_stats()

        if week == 6:
                print("\n📚 MIDTERM EXAM")
                if p.grades >= 70:
                    p.grades += 10
                    print("Excellent performance!")
                elif p.grades >= 50:
                    p.grades += 5
                    print("Average performance.")
                else:
                    p.grades -= 10
                    print("Poor performance.")

        if week == 8:
                print("\n💼 Internship Opportunity!")
                ans = input("Apply? (yes/no): ").lower()
                if ans == "yes":
                    if p.grades >= 70:
                        print("You got the internship!")
                        p.money += 300
                        p.happiness += 10
                    else:
                        print("Application rejected.")
                        p.happiness -= 5

        print("\nActions")
        print("1. Study")
        print("2. Part-Time Job")
        print("3. Rest")
        print("4. Hang Out")
        print("5. Campus Shop")


        action = input("Choose: ")

        if action == "1":
            p.study()

        elif action == "2":
            p.work()

        elif action == "3":
            p.rest()

        elif action == "4":
            p.hangout()

        elif action == "5":
            p.shop()

        else:
            print("Invalid action.")
            continue

        random_event(p)

        check_achievements(p)

        if p.health <= 0:
            print("\n😫 BURNOUT ENDING")
            break

        if p.money <= 0:
            print("\n💸 FINANCIAL CRISIS ENDING")
            break

    print("\n📝 FINAL EXAMS")

    if p.grades >= 80:
            p.grades += 15
            print("You aced your finals!")
    elif p.grades >= 60:
            p.grades += 5
            print("You passed your finals.")
    else:
            p.grades -= 10
            print("You struggled in finals.")

    print("\n🎉 Semester Complete!")
    p.show_stats()

    print("\nAchievements:")
    for a in p.achievements:
        print("-", a)

    if p.grades >= 90 and p.health >= 80 and p.happiness >= 80:
            print("\n🌟 LEGENDARY STUDENT ENDING 🌟")
    elif p.grades >= 90 and p.health >= 50:
            print("\n🏅 HONORS STUDENT ENDING")
    elif p.grades >= 60:
            print("\n🎓 SUCCESSFUL GRADUATION ENDING")
    else:
            print("\n😭 FAILED SEMESTER ENDING")

while True:
    play_game()
    again = input("\nPlay Again? (yes/no): ").lower()
    if again != "yes":
        break
