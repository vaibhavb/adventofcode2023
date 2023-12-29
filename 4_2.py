import sys
import os
from typing import List


def get_card_values(cardlines):
    card_copies = [1 for _ in cardlines]
    for idx, card in enumerate(cardlines):
        cardno = card.split(':')[0]
        cardnum = cardno.split(' ')[-1]
        rest = card.split(':')[1]
        winning_numbers = rest.strip().split('|')[0]
        win_nums = winning_numbers.strip().split(' ')
        my_numbers = rest.strip().split('|')[1]
        my_nums = my_numbers.strip().split(' ')
        values: list[int] = []
        for my_num in my_nums:
            if my_num != '':
                if my_num in win_nums:
                    # update the number of insert cards as copies
                    values.append(int(my_num))
        for _ in range(0, card_copies[idx]):
            for copy_idx, _ in enumerate(values):
                card_copies[idx + copy_idx + 1] += 1
        print(f"{idx}: {len(values)}")
    for idx, card_value in enumerate(card_copies):
        print(f"{idx}: {card_value}")
    total = sum(card_copies)
    print(f"The total : {total}")

if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = (os.path.basename(__file__)
                    .replace("py", "in")
                    .replace("_2", ""))
    cardlines: list[str] = open(filename).read().strip().split('\n')
    get_card_values(cardlines)
