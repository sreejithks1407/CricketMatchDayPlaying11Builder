import random


def pick_pacers(available_pacers, number_of_pacers_needed) -> list:

    choosen_pacers = 0
    pacers_lineup = []

    while choosen_pacers < number_of_pacers_needed:
        random_number = random.randint(0, len(available_pacers)-1)
        random_player = available_pacers.pop(random_number)
        pacers_lineup.append(random_player)
        choosen_pacers += 1

    return pacers_lineup
