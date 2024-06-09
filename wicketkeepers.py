import random


def pick_wicketkeeper(available_wicketkeepers) -> list:

    wicketkeeper = []

    random_number = random.randint(0, len(available_wicketkeepers)-1)
    random_player = available_wicketkeepers.pop(random_number)
    wicketkeeper.append(random_player)

    return wicketkeeper
