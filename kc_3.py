
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



data = pd.read_excel('JCPS_Homeless_Students.xlsx', sheet_name='20-21 Elementary', usecols= [1,9,10,11], nrows = 89)

# Replaced the * in the Male and Female columns with 0
data['Male'] = data['Male'].replace('*','0')

data['Female'] = data['Female'].replace('*','0')

#Changed data type from str to int
data["Male"] = data["Male"].astype(str).astype(int)

data["Female"] = data["Female"].astype(str).astype(int)
 
def percentages(df):
    """This function returns the percentage of homeless students that are male for 
    Elementary Schools. 
    
    Inputs:
    -------
    df : DataFrame object, a dataframe with columns School, Male, Female
    
    Returns:
    -------
    What percent of the homeless students are male."""

    num_males = sum(df.Male)
    total_homeless = sum(df['Total Homeless Count'])
    percent_male_homeless_stu = (num_males/total_homeless)*100
    return percent_male_homeless_stu

percentages(data)

print(round(percentages(data)), "percent of the homeless students in JCPS are male.")

def chart(df):
    """A pie chart of the homeless male vs female student percents

    Inputs:
    -------
    df : DataFrame object,  a dataframe with columns School, Male, Female
    
    Returns:
    -------
    Pie Chart"""

    males_num = sum(df.Male)
    total_homeless_num = sum(df['Total Homeless Count'])
    male_homeless_stu_percent = (males_num/total_homeless_num)*100
    num_females = sum(df.Female)
    female_homeless_stu_percent = (num_females/total_homeless_num)*100
    cumul_data = [male_homeless_stu_percent, female_homeless_stu_percent]

    return cumul_data

print(chart(data))


plt.pie(chart(data), labels = ['Male', 'Female'], autopct='%1.1f%%')
plt.show()






