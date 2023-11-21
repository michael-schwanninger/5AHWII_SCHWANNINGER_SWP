import sys

from statistic import statistics
from charts import create_chart


def play():
    stats = statistics(int(sys.argv[1]))
    print(stats[0])
    print("\ndeviation from wiki data:\n")
    print(stats[1])
    create_chart(stats[0])


if __name__ == "__main__":
    play()

