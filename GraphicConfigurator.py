import matplotlib.pyplot as plt


def configure_standard_graphic_settings():
    plt.figure(figsize=(15, 15))
    plt.axvline(x=0, c='green')
    plt.axhline(y=0, c='red')


def set_title(title):
    plt.title(title)


def set_axis_labels(x_label, y_label):
    plt.xlabel(x_label)
    plt.ylabel(y_label)


def set_axis_limits(x_start, x_end, y_start, y_end):
    plt.xlim(x_start, x_end)
    plt.ylim(y_start, y_end)


def set_x_ticks(x_points):
    plt.xticks(x_points)


def set_y_ticks(y_points):
    plt.yticks(y_points)


def add_graphic(x, y, color=None):
    if color is not None:
        plt.plot(x, y, color)
    else:
        plt.plot(x, y)


def add_scatter(x, y, color, label):
    plt.scatter(x, y, c=color, label=label)


def configure_standard_legend():
    plt.legend(scatterpoints=1,
               loc='upper left',
               ncol=1,
               fontsize=14)
