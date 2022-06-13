import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

GA_data = pd.read_excel(r'C:\Users\gduncan\OneDrive - Metro United Way, Inc. (191100)\Desktop\Professional Development\Python\Code_Louisville\data_1_checks\assets\GeneralAssembly.xlsx')

GA_data_by_career = GA_data.groupby('Which career path did you choose with General Assembly?')['Respondent ID'].nunique()

print(GA_data_by_career)

career = ['Data Analytics', 'Digital Marketing', 'Front End Web Dev', 'UX Design']
num_of_students = [58, 14, 10, 21]


plt.style.use('dark_background')
plt.figure(figsize = (12,6))

plt.bar(career, num_of_students)
plt.xlabel('Career Type')
plt.ylabel('Number of Students')
plt.title('Careers Chosen by Graduates')

plt.show()
