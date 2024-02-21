import sys
from statistic import statistics
from charts import create_chart


def play():
    rounds = int(sys.argv[1]) if len(sys.argv) > 1 else 100000
    stats = statistics(rounds)
    print(stats[0])
    print("\nDeviation from wiki data:\n")
    print(stats[1])
    create_chart(stats[0])


if __name__ == "__main__":
    play()

