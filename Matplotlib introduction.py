
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
import numpy as np


df_dowjones = sns.load_dataset('dowjones') 
# https://fred.stlouisfed.org/series/M1109BUSM293NNBR
df_penguins = sns.load_dataset('penguins')
# https://github.com/allisonhorst/palmerpenguins

###############################################
# Create simple line plot

df_dowjones.info()

plt.plot(df_dowjones.Date, df_dowjones.Price);

# Add title and labels

plt.plot(df_dowjones.Date, df_dowjones.Price)
plt.xlabel('$Year$')
plt.ylabel('$Price$')
plt.title('Dow-Jones Industrial Stock Price Index for United States')


# Comparison

df_dowjones.shape

df_dowjones['Error1'] = df_dowjones.Price + 100
df_dowjones['Error2'] = df_dowjones.Price - 100

plt.plot(df_dowjones.Date, df_dowjones.Price, label = 'Original price')
plt.plot(df_dowjones.Date, df_dowjones.Error1, label = 'Positive margin')
plt.plot(df_dowjones.Date, df_dowjones.Error2, label = 'Negative margin')
plt.xlabel('$Year$')
plt.ylabel('$Price$')
plt.title('Dow-Jones Industrial Stock Price Index for United States')
plt.tight_layout() # Check info: padding (almohadillas, margenes )
plt.legend(loc = 'upper left') # Check info

# Customization

plt.plot(df_dowjones.Date, df_dowjones.Error1, label = 'Positive margin', 
         color = 'midnightblue', linewidth = .5, linestyle = '--')
plt.plot(df_dowjones.Date, df_dowjones.Error2, label = 'Negative margin', 
         color = 'midnightblue', linewidth = .5, linestyle = '--')
plt.plot(df_dowjones.Date, df_dowjones.Price, label = 'Original price',
         color = 'darkorchid', linewidth = 1)
plt.xlabel('$Year$')
plt.ylabel('$Price$')
plt.title('Dow-Jones Industrial Stock Price Index for United States')
plt.legend(loc = 'upper left') # Check info

# Hex color: check!

# Font size

plt.plot(df_dowjones.Date, df_dowjones.Error1, label = 'Positive margin', 
         color = 'midnightblue', linewidth = .5, linestyle = '--')
plt.xlabel('$Year$', fontsize = 25)
plt.ylabel('$Price$', fontsize = 12)
plt.title('Dow-Jones Industrial Stock Price Index for US', fontsize = 12)


plt.figure(figsize= (8,4))
plt.plot(df_dowjones.Date, df_dowjones.Error1, label = 'Positive margin', 
         color = 'midnightblue', linewidth = .5, linestyle = '--')
plt.xlabel('$Year$')
plt.ylabel('$Price$')
plt.title('Dow-Jones Industrial Stock Price Index for US')
plt.grid(linestyle='--')

#########################################################
###################### Subplots #########################
#########################################################

fig, ax = plt.subplots(nrows=2, ncols=3)
# print(ax)

fig, ax = plt.subplots(2, 3, sharex='col', sharey='row')

fig, (ax1, ax2) = plt.subplots(nrows= 2, ncols= 1)
ax1.plot(df_dowjones.Date, df_dowjones.Error1, label = 'Positive margin', 
         color = 'midnightblue', linewidth = .5, linestyle = '--')
ax1.plot(df_dowjones.Date, df_dowjones.Error2, label = 'Negative margin', 
         color = 'midnightblue', linewidth = .5, linestyle = '--')
ax2.plot(df_dowjones.Date, df_dowjones.Price, label = 'Original price',
         color = 'darkorchid', linewidth = 1)

ax1.set_xlabel('Date')
ax1.set_ylabel('Price')
ax1.set_title('Errors margin')

ax2.set_xlabel('Date')
ax2.set_ylabel('Price')
ax2.set_title('Original price')


ax1.grid(linestyle = '--')
ax2.grid(linestyle = '--')
plt.tight_layout() # Esto ayuda a espaciarlos
# plt.savefig('grafico.pdf')
