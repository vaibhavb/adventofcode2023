import sys

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
        #print(f"values: {values}, total: {len(values)}")
        #card_values[int(cardnum)] = val_idx[len(values)]
        card_values_total += val_idx[len(values)]
        print(f"{cardnum}: {val_idx[len(values)]}")
    return card_values_total


if __name__ == "__main__":
   filename = sys.argv[1]
   cardlines = open(filename).read().strip().split('\n')
   print(get_card_values(cardlines))
