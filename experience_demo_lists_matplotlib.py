# import module (library) dependencies so we can use their classes and functions
# we are only going to use matplotlib for creating the histograms
# we will do everything else from scratch (e.g. with only built-in python functionality)
import os
import matplotlib.pyplot as plt 

file_path = os.path.join("..", "WelcomeQuestionnaireExperienceData", "322_welcome_questionnaire_demo.csv")
infile = open(file_path, "r")

# read csv file data into table format (nested list)
table = []
for line in infile.readlines():
    line = line.strip()
    values = line.split(",")
    table.append(values)

# remove the first row from numeric part of the table, it is the header row with column labels
header = table.pop(0)

# convert string vals in the table to numeric
for row in table:
    for i in range(len(row)):
        try: # try converting value to numeric int type
            row[i] = int(row[i])
        except: # if can't convert to integer
            row[i] = 3 # fill with middle value

# create a figure with 6 axes all in a row
fig, ax = plt.subplots(1, 6, sharex=True, sharey=True) # one row, four columns
ax[0].set_xticks([1.5, 2.5, 3.5, 4.5, 5.5])
ax[0].set_xticklabels(["1", "2", "3", "4", "5"])
ax[0].set_xlim([1, 6])
ax[0].set_ylabel("Student Count")

# can easily index to get a single row... but what about getting a single column?
# use list comprehensions! (one liner loops to build a list)
# do this for each experience category (4 in total) in a loop (so we don't have redundant code)
colors = ["blue", "orange", "green", "red", "purple", "gray"]
for i in range(len(header)):
    ax[i].hist([row[i] for row in table], bins=[1, 2, 3, 4, 5, 6], edgecolor="black", facecolor=colors[i])
    ax[i].set_title(header[i])
    ax[i].set_xlabel("Likert Response")

# setting the size to make it look more like the seaborn facet grid output
fig.set_size_inches(10, 3.5)
plt.tight_layout()
file_path = os.path.join("..", "WelcomeQuestionnaireExperienceData", "322_experience_matplotlib.png")
plt.savefig(file_path)
