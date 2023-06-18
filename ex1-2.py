import matplotlib.pyplot as plt

def create_scatterplot(x, y):
    """TODO: Create a scatterplot using the plt.scatter() function with x and y as the data inputs.
    Label the x-axis with "X Values" and the y-axis with "Y Values". Add a title to the plot that says
    "Scatterplot of X and Y"."""

    #TASK START - Start coding here:
    plt.scatter(x,y)
    plt.xlabel("X Values")
    plt.ylabel("Y Values")
    plt.title("Scatterplot of X and Y")
    plt.show()
    # TASK END


#TASK START - Start coding here:

# Create Your x and y data points:
import random
x = []
y = []

for i in range(0,7):
    n = random.randint(1,100)
    x.append(n)
    y.append(n)

# Call out the create_scatterplot function:
create_scatterplot(x, y)
# TASK END