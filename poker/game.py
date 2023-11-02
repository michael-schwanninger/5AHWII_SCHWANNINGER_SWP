import random

# - 11 - J
# - 12 - K
# - 13 - A

# //13 for color | %13 for value

card_deck = [i for i in range(52)]


def getColor(card):
    return card // 13


def getValue(card):
    return card % 13


def poker_hands(cards):
    cards.sort()

    # - Flush - 5 of the same color
    colors = [getColor(card) for card in cards]
    colors.sort()
    flush = colors[0] == colors[4]

    # set -> only unique items (only works with 5 cards drawn)
    #flush = len(set(colors)) == 1

    # - Straight - 5 consecutive numbers
    values = [getValue(card) for card in cards]
    values.sort()
    straight = True
    for i in range(0, 4):
        if values[i] != values[i + 1] - 1:
            straight = False

    # - n_of_a_Kind
    value_counter = [0] * 13
    for card in cards:
        value_counter[getValue(card)] += 1

    four_of_a_kind = 4 in value_counter
    three_of_a_kind = 3 in value_counter
    two_pair = value_counter.count(2) == 2  # checks if there are two pairs
    pair = 2 in value_counter

    if flush and straight and cards[0] == 8:
        return "royal_flush"
    elif flush and straight:
        return "straight_flush"
    elif four_of_a_kind:
        return "four_of_a_kind"
    elif three_of_a_kind and pair:
        return "full_house"
    elif flush:
        return "flush"
    elif straight:
        return "straight"
    elif three_of_a_kind:
        return "three_of_a_kind"
    elif two_pair:
        return "two_pair"
    elif pair:
        return "pair"
    else:
        return "highest_card"


def statistics(rounds):
    stats = {
        "royal_flush": 0,
        "straight_flush": 0,
        "four_of_a_kind": 0,
        "full_house": 0,
        "flush": 0,
        "straight": 0,
        "three_of_a_kind": 0,
        "two_pair": 0,
        "pair": 0,
        "highest_card": 0,
    }

    for i in range(rounds):
        deck = card_deck.copy()
        random.shuffle(deck)
        hand = deck[:5]
        result = poker_hands(hand)
        stats[result] += 100 / rounds

    return stats


if __name__ == "__main__":
    print(statistics(100000))
