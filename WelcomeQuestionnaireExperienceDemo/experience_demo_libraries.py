# import module (library) dependencies so we can use their classes and functions
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

# open the CSV file and load its data into a Pandas Dataframe
dataframe = pd.read_csv("322_welcome_questionnaire_demo.csv")
# this is a cool feature of a pandas dataframe where you can quickly see a summary of the frame
print(dataframe.describe())

# unpivot 4 dataframe columns into long format
dataframe = dataframe.melt(var_name="Experience", value_name="Likert Response")

# plot each experience on its own axis in a grid using Seaborn
g = sns.FacetGrid(dataframe, col="Experience", hue="Experience")
g.map(sns.histplot, "Likert Response", bins=[1, 2, 3, 4, 5, 6])
g.set(xticks=[1.5, 2.5, 3.5, 4.5, 5.5], xticklabels=["1", "2", "3", "4", "5"])
g.axes[0,0].set_ylabel("Student Count")

# save to a file
plt.tight_layout()
plt.savefig("322_experience_sns.png")