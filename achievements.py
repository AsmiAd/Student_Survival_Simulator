def check_achievements(player):

    if player.grades >= 100:
        if "Academic Weapon" not in player.achievements:
            player.achievements.append("Academic Weapon")
            print("\n🏆 Achievement Unlocked: Academic Weapon")

    if player.money >= 1000:
        if "Money Master" not in player.achievements:
            player.achievements.append("Money Master")
            print("\n🏆 Achievement Unlocked: Money Master")

    if player.health >= 100:
        if "Fitness Freak" not in player.achievements:
            player.achievements.append("Fitness Freak")
            print("\n🏆 Achievement Unlocked: Fitness Freak")

    if player.happiness >= 100:
        if "Social Butterfly" not in player.achievements:
            player.achievements.append("Social Butterfly")
            print("\n🏆 Achievement Unlocked: Social Butterfly")