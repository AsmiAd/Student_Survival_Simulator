import random
from data import EVENTS

def random_event(player):

    event = random.choice(EVENTS)

    title = event[0]
    stat = event[1]
    amount = event[2]

    print("\nRANDOM EVENT:")
    print(title)

    if stat == "grades":
        player.grades += amount

    elif stat == "health":
        player.health += amount

    elif stat == "money":
        player.money += amount

    elif stat == "happiness":
        player.happiness += amount

    elif stat == "stress":
        player.stress += amount