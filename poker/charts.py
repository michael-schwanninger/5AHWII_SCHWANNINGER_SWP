from matplotlib import pyplot as plt

def create_chart(data):
    plt.pie(data.values(), labels=data.keys())
    plt.show()