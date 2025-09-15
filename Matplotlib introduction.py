
# Introduction to data cizualization

'''
In statistics, we generally have two kinds of visualization:

Exploratory data visualization: 
    Exploring the data visually to find patterns among the data entities.

Explanatory data visualization: 
    Showcasing the identified patterns using simple graphs.

'''

# Matplotlib

# Figure and axes
# The entire illustration is called a figure and each plot on it
# is an axes (do not confuse Axes with Axis)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df_dowjones = sns.load_dataset('dowjones') 
# https://fred.stlouisfed.org/series/M1109BUSM293NNBR
df_penguins = sns.load_dataset('penguins')
# https://github.com/allisonhorst/palmerpenguins

# Create simple line plot

df.info()

plt.plot(df.body_mass_g);

plt.plot()

# Add Title, labels

plt.plot(ages,mib_salary)
plt.xlabel('$Ages$')
plt.ylabel('$Median Salary (USD)$')
plt.title('$Median Salary (USD) by Age$')
plt.show()


# Comparison

# Microbiolog