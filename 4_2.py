import sys
import os
from typing import List

def get_card_values(cardlines):
    card_values = []
    card_values_total = 0
    val_idx = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
    for card in cardlines:
        cardno = card.split(':')[0]
        cardnum = cardno.split(' ')[-1]
        rest = card.split(':')[1]
        winning_numbers = rest.strip().split('|')[0]
        win_nums = winning_numbers.strip().split(' ')
        my_numbers = rest.strip().split('|')[1]
        my_nums = my_numbers.strip().split(' ')
        values = []
        for my_num in my_nums:
            if my_num != '':
                if my_num in win_nums:
                    values.append(my_num)
        # print(f"values: {values}, total: {len(values)}")
        card_values.append(val_idx[len(values)])
        card_values_total += val_idx[len(values)]
    for idx, card_value in enumerate(card_values):
        print(f"{idx}: {card_value}")
    return card_values_total


if __name__ == "__main__":
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = (os.path.basename(__file__)
                    .replace("py", "in")
                    .replace("_1", ""))
    cardlines: list[str] = open(filename).read().strip().split('\n')
    print(get_card_values(cardlines))
