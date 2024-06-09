import random


def pick_spinners(available_spinners, number_of_spinners_needed) -> list:

    choosen_spinners = 0
    spinners_lineup = []

    while choosen_spinners < number_of_spinners_needed:
        random_number = random.randint(0, len(available_spinners)-1)
        random_player = available_spinners.pop(random_number)
        spinners_lineup.append(random_player)
        choosen_spinners += 1

    return spinners_lineup
