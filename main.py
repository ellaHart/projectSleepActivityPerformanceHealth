import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import statsmodels.api as sm


# ^ pre populated text suggestions


# v analysis


# Load your data (replace 'your_data.csv' with your actual file)
data = pd.read_csv("dataset.py") 

# You can inspect the names of all columns below (if the output is too long, you can click on the button on the left of the output to hide the lengthy output)
for col in data.columns:
  print(col)

# Check for missing values
data.info()

# Describe numerical data
data.describe()

# Visualize relationships
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

# Calculate correlations
corr_sleepsd_stress = stats.pearsonr(data['sleepsd'], data['preexamstress'])
corr_stepsave_stress = stats.pearsonr(data['stepsave'], data['preexamstress'])
print(f"Correlation between sleep variability and pre-exam stress: {corr_sleepsd_stress}")
print(f"Correlation between average daily steps and pre-exam stress: {corr_stepsave_stress}")

# Conduct hypothesis tests
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


# conclusion

# Correlation test between sleep variability and homework grades
corr, p_value = stats.pearsonr(data['sleepsd'], data['psetz'])
print(f"Correlation: {corr}, P-value: {p_value}")


# ### Conclusion
# The analysis suggests that there is a significant negative correlation between sleep variability and homework grades, meaning that students with more consistent sleep patterns tend to perform better academically. This aligns with findings in previous research on the importance of sleep consistency. Further exploration could investigate additional mental health outcomes, such as self-reported stress levels, in relation to both physical activity and sleep.
