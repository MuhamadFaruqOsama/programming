import numpy as np
import pandas as pd

# creating data frame uisng pandas using students variable
students = ['faruq','adiknya faruq','kakaknya faruq','saudaranya faruq']
students_df = pd.DataFrame(students, columns=['students'])

grade = ['A','A-','A+','A']
# df = pd.DataFrame({'Students':students, 'Grade':grade})
# print(df)

# creating data frame using pandas series
year = pd.Series([2012,2013,2014,2015,2016,2017,2018])
energy_consumption = pd.Series([2152,2196,2217,2194,2172,2180,2258])

df = pd.DataFrame({'Year':year,'Energy Consumption':energy_consumption})
# print(df)

# creating data frame using random number
random_df = pd.DataFrame(np.random.randn(5,2), columns=['Trial 1', 'Trial 2'])
print(random_df)