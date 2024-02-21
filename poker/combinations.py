from Aufgaben.poker.timer_decorator import timer


# - 0 - 2
# - 1 - 3
# - 2 - 4
# - 3 - 5
# - 4 - 6
# - 5 - 7
# - 6 - 8
# - 7 - 9
# - 8 - 10
# - 9 - J
# - 10 - Q
# - 11 - K
# - 12 - A


# //13 for color | %13 for value


def getColor(card):
    return card // 13


def getValue(card):
    return card % 13


@timer
def poker_hands(cards):
    cards.sort()

    # - Flush - 5 of the same color
    colors = [getColor(card) for card in cards]
    colors.sort()
    flush = colors[0] == colors[4]

    # - Straight - 5 consecutive numbers or with ace -> 12, 0, 1, 2, 3
    values = [getValue(card) for card in cards]
    values.sort()
    straight = (
        all(values[i] == values[i + 1] - 1 for i in range(4)) or  # Consecutive values
        values == [0, 1, 2, 3, 12]  # Special case: Ace, 2, 3, 4, 5
    )

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
