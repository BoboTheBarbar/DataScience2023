# Import Library Here
import matplotlib.pyplot as plt

# Create a histogram here
def create_histogram(data):
    """TODO: Create a histogram using the plt.hist() function with 'data' as the data input.
    Label the x-axis with "Values" and the y-axis with "Frequency". Add a title to the plot that
    says "Histogram of My Sequence"."""

    #TASK START - Start coding here:
    plt.hist(data)
    plt.xlabel("Values")
    plt.ylabel("Frequency")
    plt.title("Histogram of My Sequence")
    plt.show()
    # TASK END


def create_line_plot(data):
    """ TODO: Create a line plot using the plt.plot() function with 'data' as the data input.
    Label the x-axis with "Index" and the y-axis with "Values". Add a title to the plot that says
    "Line Plot of My Sequence" """

    #TASK START - Start coding here:
    plt.plot(data)
    plt.xlabel("Index")
    plt.ylabel("Values")
    plt.title("Line Plot of My Sequence")
    plt.show()
    # TASK END

#TASK START - Start coding here:

# Create Your data sequence:
import random
data = []

for i in range(0,7):
    n = random.randint(1,100)
    data.append(n)

# Call out the create_histogram function:
print(data)
create_histogram(data)
# Call out the create_line_plot function:
create_line_plot(data)

# TASK END