import random


def pick_batters(available_batters, number_of_batters_needed) -> list:

    choosen_batters = 0
    batting_lineup = []

    while choosen_batters < number_of_batters_needed:
        random_number = random.randint(0, len(available_batters)-1)
        random_player = available_batters.pop(random_number)
        batting_lineup.append(random_player)
        choosen_batters += 1

    return batting_lineup
