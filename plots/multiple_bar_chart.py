import os, pdb
from matplotlib import pyplot as plt


def bar_plot(ax, data, colors=None, total_width=0.8, single_width=1, legend=True):
    """Draws a bar plot with multiple bars per data point.

    """

    # Check if colors where provided, otherwhise use the default color cycle
    if colors is None:
        colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

    # Number of bars per group
    n_bars = len(data)

    # The width of a single bar
    bar_width = total_width / n_bars

    # List containing handles for the drawn bars, used for the legend
    bars = []

    # Iterate over all data
    for i, (name, values) in enumerate(data.items()):
        # The offset in x direction of that bar
        x_offset = (i - n_bars / 2) * bar_width + bar_width / 2

        # Draw a bar for every value of that type
        for x, y in enumerate(values):
            bar = ax.bar(x + x_offset, y, width=bar_width * single_width, color=colors[i % len(colors)])

        # Add a handle to the last drawn bar, which we'll need for the legend
        bars.append(bar[0])

    # Draw legend if we need
    if legend:
        ax.legend(bars, data.keys())

    plt.xlabel('Evaluation Set')
    plt.ylabel('EER')
    plt.grid(axis='y')
    plt.xticks([0,1,2], ['VoxCeleb1', 'VoxMovies\n(Same Movie Positives)', 'VoxMovies\n(Different Movie Positives)'])



if __name__ == "__main__":
    # Usage example:
    # data = {
    #     "VoxCeleb1": [5.53, 16.6, 21.5, 3.30, 2.05, 1.05],
    #     "VoxMovies - Same Movie Positives": [16.6, 12.92, 9.72, 6.09],
    #     "VoxMovies - Different Movie Positives": [21.5, 17.97, 14.11, 10.47],
    # }
    data = {
        "I-Vector": [5.53, 16.6, 21.5],
        "X-Vector": [3.30, 12.92, 17.97],
        "Thin-ResNet34": [2.05, 9.72, 14.11],
        "Thick-ResNet34": [1.05, 6.09, 10.47],
    }

    fig, ax = plt.subplots()
    bar_plot(ax, data, total_width=.8, single_width=.9)
    plt.show()
