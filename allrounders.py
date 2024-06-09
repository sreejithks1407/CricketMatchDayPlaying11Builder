import random


def pick_allrounders(available_allrounders, number_of_allrounders_needed) -> list:

    choosen_allrounders = 0
    allrounders_lineup = []

    while choosen_allrounders < number_of_allrounders_needed:
        random_number = random.randint(0, len(available_allrounders)-1)
        random_player = available_allrounders.pop(random_number)
        allrounders_lineup.append(random_player)
        choosen_allrounders += 1

    return allrounders_lineup
