## First step, save this notebook to your own google drive

Click on "File" button on the top-left, then click the button "Save a copy in Drive".

It might open up a new window for the saved copy. If not, click the "Open notebook" button under "File" menu to select the copy you just saved.


This way, all your edits will be saved in your google drive, and you can continue to work on it the next day.

But remember, if you re-open a notebook after closing it, you need to run all the code blocks to make sure packages are imported and data are loaded, in order to continue.


### Project introduction
In this project, you can use a dataset created by Prof. Gregory Samanez-Larkin at Duke University to investigate how sleep and amount of physical activity may be related to academic performance (grades for homework assignment et.,) and mental health (e.g., feeling of tiredness and stress).

The dataset was collected by Fitbits on activity (number of steps taken by a student) and sleep as well as some data related to academic performance in a class and in general. You can use the dataset to examine how overall amount of steps and sleep are related to academic outcomes, or evaluate the effects of sleep variability (the opposite of sleep consistency) on academic outcomes. Studies have shown that sleep variability is more strongly related to grades than overall sleep. Of course, you can also ask any other interesting questions from this dataset.



To load the dataset, please run the following command.
import pandas as pd
data = pd.read_csv("https://raw.githubusercontent.com/lcnature/PSY292_2024Fall/refs/heads/main/final_project/datasets/sleep_mental/stepsleepacademics.csv")
You can inspect the names of all columns below (if the output is too long, you can click on the button on the left of the output to hide the lengthy output)

for col in data.columns:
  print(col)
### Meaning of each column
Below is the description of these variables:

student: participant ID number

stepsave: average daily steps across all days

stepslmh: categorical version of stepsave where 1 = lowest third of average steps, 2 = middle third of average steps, and 3 = highest third of average steps

stepssd: mean-squared successive differences across all adjacent days where step data were available

stepssdlmh: categorical version of stepssd where 1 = lowest third of step variability, 2 = middle third of step variability, and 3 = highest third of step variability

sleepave: average minutes of sleep across all days

sleeplmh: categorical version of sleepave where 1 = lowest third of average sleep, 2 = middle third of average sleep, and 3 = highest third of average sleep

sleepsd: mean-squared successive differences across all adjacent days where sleep data were available

sleepsdlmh: categorical version of sleepsd where 1 = lowest third of sleep variability, 2 = middle third of sleep variability, and 3 = highest third of sleep variability

female: 1 = female, 0 = male

psetz: z-standardized average of weekly homework assignment grades across the semester

psetz_minus3lowest: same as psetz but lowest 3 scores removed to evaluate robustness of effects to potential outliers

understandse: self-reported rating of how well the student understand the concept of standard error after the first lecture introducing the concept, 1-7 Likert scale where higher scores are better understanding

corrguesserror: average error scores after playing one round of guessthecorrelation.com higher scores are worse guesses at the correlation depicted in scatterplots

hwcondiff: self-reported difficulty concentrating while doing homework assignments on 1-7 Likert scale where higher scores are more difficulty concentrating

leccondiff: self-reported difficulty concentrating during lecture on 1-7 Likert scale where higher scores are more difficulty concentrating

lecturetired: self-reported tiredness at the beginning of class on a 1-7 Likert scale where higher scores are more tired

preexamstress: self-reported stress level before an exam on 1-7 Likert scale where higher scores are higher levels of stress


## Your task
This is an open-ended assignment.

Your task is to ask one or a few questions raised by yourself by analyzing the dataset.

You will write your own text cell explaining your question. Then your notebook can interleave between code cells that analyze the data and text cells that explain what you are doing.

At the end, please use the "Download" button in "File" menu to download the notebook as ipynb file to submit. Please also either use the "Print" button in "Menu" to print a pdf of the notebook, or, if it does not work, take a few screenshots of each portion and paste into a word document to submit.

**Please submit both your notebook as ipynb file and pdf/screenshots to Blackboard.**

Your report should contain at least:
- one visualization of the data in relation to your question, in any way you choose.
- applying one statistical technique you learned in class.
- drawing a conclusion based on the outcome of the analysis (it does not matter if you don't find any significant effect).

Evaluation criteria:
- concise and clear description of your question and what your code does.
- proper labeling of your figure(s) (e.g., labels for axes. `plt.xlabel()` is one example command)
- proper usage of the tool you use.
- proper conclusion based on the result.

I pre-populated a few text sections below and loaded packages that you may use. Feel free to change the titles of each section, and find and use other packages.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import statsmodels.api as sm

# My question / hypothesis
How is pre-exam stress affected by sleep variability or daily step count?

# Analysis

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
sns.scatterplot(x='sleepsd', y='preexamstress', data=data)
plt.xlabel('Sleep Variability (sleepsd)')
plt.ylabel('Pre-Exam Stress (preexamstress)')
plt.title('Sleep Variability vs. Pre-Exam Stress')

plt.subplot(1, 2, 2)
sns.scatterplot(x='stepsave', y='preexamstress', data=data)
plt.xlabel('Average Daily Steps (stepsave)')
plt.ylabel('Pre-Exam Stress (preexamstress)')
plt.title('Average Daily Steps vs. Pre-Exam Stress')

plt.tight_layout()
plt.show()

#calculations of correlations
corr_sleepsd_stress = stats.pearsonr(data['sleepsd'], data['preexamstress'])
corr_stepsave_stress = stats.pearsonr(data['stepsave'], data['preexamstress'])
print(f"Correlation between sleep variability and pre-exam stress: {corr_sleepsd_stress}")
print(f"Correlation between average daily steps and pre-exam stress: {corr_stepsave_stress}")

#hypothesis tests
alpha = 0.05
p_value_sleepsd = corr_sleepsd_stress[1]
p_value_stepsave = corr_stepsave_stress[1]

print(f"P-value for sleep variability: {p_value_sleepsd}")
print(f"P-value for average daily steps: {p_value_stepsave}")

if p_value_sleepsd < alpha:
    print("There is a significant correlation between sleep variability and pre-exam stress.")
else:
    print("There is no significant correlation between sleep variability and pre-exam stress.")

if p_value_stepsave < alpha:
    print("There is a significant correlation between average daily steps and pre-exam stress.")
else:
    print("There is no significant correlation between average daily steps and pre-exam stress.")
# Conclusion
# Correlation test between sleep variability and homework grades
corr, p_value = stats.pearsonr(data['sleepsd'], data['psetz'])
print(f"Correlation: {corr}, P-value: {p_value}")

### Conclusion
The analysis suggests that there is a significant negative correlation between sleep variability and homework grades, meaning that students with more consistent sleep patterns tend to perform better academically. This aligns with findings in previous research on the importance of sleep consistency. Further exploration could investigate additional mental health outcomes, such as self-reported stress levels, in relation to both physical activity and sleep.
