import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pydataset import data

# Use the iris database to answer the following quesitons:

#     What does the distribution of petal lengths look like?

iris = sns.load_dataset("iris")
print(iris.describe())
# plt.figure(figsize=(12, 10))
# sns.pairplot(iris)
# plt.show()

#     Is there a correlation between petal length and petal width? 
#     Use http://guessthecorrelation.com/ as a hint to how we could visually determine if a 
#     correlation exists between two numeric columns.

# Yes, there seems to be a strong correlation between petal length/width.

#     Would it be reasonable to predict species based on sepal width and sepal length?
#     For this, you'll visualize two numeric columns through the lense of a categorical column.

# No, the correlation is very weak.

#     Which features would be best used to predict species?

# It would be best to predict the iris species based on petal length/width. There are probably other features
# best suited for identifcation besides those in the dataframe (e.g. - color, crest, beard, etc.)

#     Using the lesson as an example, use seaborn's load_dataset function to load the anscombe data set. 
#     Use pandas to group the data by the dataset column, and calculate summary statistics for each dataset. 
#     What do you notice?

ans = sns.load_dataset("anscombe")
print(ans.info())
ans.groupby(["dataset"])
print(ans.describe())

#     Plot the x and y values from the anscombe data. Each dataset should be in a separate column.

# sns.pairplot(ans)
# plt.show()

#     Load the InsectSprays dataset and read it's documentation. 
#     Create a boxplot that shows the effectiveness of the different insect sprays.

spray = data("InsectSprays")
# data("InsectSprays", show_doc = True)
# print(spray.info())

# sns.boxplot(data = spray, y = "count", x = "spray")
# plt.show()

#     Load the swiss dataset from pysdataset and read it's documentation.
#     Create visualizations to answer the following questions:
#       Create an attribute named is_catholic that holds a boolean value of whether or not the province is Catholic. 
#       (Choose a cutoff point for what constitutes catholic)
#       Does whether or not a province is Catholic influence fertility?
#       What measure correlates most strongly with fertility?

sws = data("swiss")
data("swiss", show_doc = True)
print(sws.info())
print(sws.head(2))

#     Using the chipotle dataset from the previous exercise, 
#     create a bar chart that shows the 4 most popular items and the revenue produced by each.

# chp = data("chipotle")
# data("chipotle", show_doc = True)
# print(chp.info())

#     Load the sleepstudy data and read it's documentation. 
#     Use seaborn to create a line chart of all the individual subject's reaction times and
#     a more prominant line showing the average change in reaction time.

# sleep = data("sleepstudy")
# data("sleepstudy", show_doc = True)
# print(sleep.info())
