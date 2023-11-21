import random
from combinations import poker_hands


def statistics(rounds):
    if int(rounds) == 0: rounds = 100000

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

    wiki_data = {
        "royal_flush": 0.000154,
        "straight_flush": 0.00139,
        "four_of_a_kind": 0.0240,
        "full_house": 0.144,
        "flush": 0.197,
        "straight": 0.392,
        "three_of_a_kind": 2.11,
        "two_pair": 4.75,
        "pair": 42.26,
        "highest_card": 50.12,
    }

    card_deck = [i for i in range(52)]

    for i in range(rounds):
        deck = card_deck.copy()
        random.shuffle(deck)
        hand = deck[:5]
        #hand = [25,12,1,2,3]
        result = poker_hands(hand)
        stats[result] += 100 / rounds

    for i in wiki_data:
        wiki_data[i] = round(stats[i] - wiki_data[i], 5)

    return stats, wiki_data
