import random
from data import EVENTS

def random_event(player):
    title, stat, amount = random.choice(EVENTS)
    print(f"\n🎲 RANDOM EVENT: {title}")

    if stat == "grades":
        player.grades += amount
        print(f"Grades {'+' if amount>0 else ''}{amount}")
    elif stat == "health":
        player.health += amount
        print(f"Health {'+' if amount>0 else ''}{amount}")
    elif stat == "money":
        player.money += amount
        print(f"Money {'+' if amount>0 else ''}{amount}")
    elif stat == "happiness":
        player.happiness += amount
        print(f"Happiness {'+' if amount>0 else ''}{amount}")
    elif stat == "stress":
        player.stress += amount
        print(f"Stress {'+' if amount>0 else ''}{amount}")
