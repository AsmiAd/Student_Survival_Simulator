from player import Player
from events import random_event
from achievements import check_achievements
from data import MAJORS

print("=" * 40)
print("🎓 STUDENT SURVIVAL SIMULATOR")
print("=" * 40)

name = input("Enter your name: ")

print("\nChoose your major:")
print("1. Computer Engineering")
print("2. Business")
print("3. Medicine")

choice = input("Choice: ")

major = MAJORS.get(choice, "Computer Engineering")

player = Player(name, major)

for week in range(1, 13):

    print(f"\n========== WEEK {week} ==========")

    player.show_stats()

    print("\nActions")
    print("1. Study")
    print("2. Part-Time Job")
    print("3. Rest")
    print("4. Hang Out")

    action = input("Choose: ")

    if action == "1":
        player.study()

    elif action == "2":
        player.work()

    elif action == "3":
        player.rest()

    elif action == "4":
        player.hangout()

    else:
        print("Invalid action.")
        continue

    random_event(player)

    check_achievements(player)

    if player.health <= 0:
        print("\n😫 BURNOUT ENDING")
        break

    if player.money <= 0:
        print("\n💸 FINANCIAL CRISIS ENDING")
        break

else:

    print("\n🎉 SEMESTER COMPLETED!")

    player.show_stats()

    print("\nAchievements Earned:")
    for achievement in player.achievements:
        print("-", achievement)

    if player.grades >= 90 and player.health >= 50:
        print("\n🏅 HONORS STUDENT ENDING")

    elif player.grades >= 60:
        print("\n🎓 SUCCESSFUL GRADUATION ENDING")

    else:
        print("\n😭 FAILED SEMESTER ENDING")