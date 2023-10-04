import random
from matplotlib import pyplot as plt


def generate_array():
    return [a for a in range(1, 45 + 1)]


def generate_random(new_range):
    return random.randrange(0, new_range)


def get_numbers(array, nbr_swaps: int):
    for i in range(nbr_swaps):
        random_index = generate_random(len(array) - 1)
        array[random_index], array[len(array) - 1 - i] = array[len(array) - 1 - i], array[random_index]
    return array[len(array) - nbr_swaps:]


def generate_dict(array):
    return dict(zip(array, [0]*len(array)))


def add_to_statistic(array, dictionary):
    for i in array:
        dictionary[i] += 1


numbers = generate_array()
number_dict = generate_dict(numbers)
for i in range(1000):
    random_numbers = get_numbers(numbers, 6)
    add_to_statistic(random_numbers, number_dict)

plt.bar(number_dict.keys(), number_dict.values())
plt.xlabel("Zahlen")
plt.ylabel("Vorkommen")
plt.show()

