import pandas as pd
import seaborn as sns

# Read titanic.csv here
titanic = pd.read_csv(".titanic.csv")

# Display the head of the dataset
titanic.head(10)

titanic_selection = titanic[["Age", "Fare", "Pclass", "Survived"]]

sns.pairplot(titanic_selection)

sns.heatmap(pd.DataFrame.corr(titanic_selection))

ages = titanic[["Age"]]

sns.histplot(ages)