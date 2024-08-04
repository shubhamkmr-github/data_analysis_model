import matplotlib.pyplot as plt

def plot_histogram(data, column):
    plt.hist(data[column])
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()

def plot_scatter(data, column1, column2):
    plt.scatter(data[column1], data[column2])
    plt.title(f'Scatter Plot of {column1} vs {column2}')
    plt.xlabel(column1)
    plt.ylabel(column2)
    plt.show()

def plot_line(data, column):
    plt.plot(data[column])
    plt.title(f'Line Plot of {column}')
    plt.xlabel('Index')
    plt.ylabel(column)
    plt.show()
