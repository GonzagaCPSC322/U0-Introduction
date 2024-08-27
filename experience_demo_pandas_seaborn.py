# import module (library) dependencies so we can use their classes and functions
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

# open the CSV file and load its data into a Pandas Dataframe
file_path = os.path.join("..", "WelcomeQuestionnaireExperienceData", "322_welcome_questionnaire_demo.csv")
dataframe = pd.read_csv(file_path)
dataframe.fillna(3, inplace=True) # fill with middle value
# this is a cool feature of a pandas dataframe where you can quickly see a summary of the frame
print(dataframe.describe())

# unpivot 6 dataframe columns into long format
dataframe = dataframe.melt(var_name="Experience", value_name="Likert Response")

# plot each experience on its own axis in a grid using Seaborn
g = sns.FacetGrid(dataframe, col="Experience", hue="Experience")
g.map(sns.histplot, "Likert Response", bins=[1, 2, 3, 4, 5, 6])
g.set(xticks=[1.5, 2.5, 3.5, 4.5, 5.5], xticklabels=["1", "2", "3", "4", "5"])
g.axes[0,0].set_ylabel("Student Count")

# save to a file
plt.tight_layout()
file_path = os.path.join("..", "WelcomeQuestionnaireExperienceData", "322_experience_seaborn.png")
plt.savefig(file_path)