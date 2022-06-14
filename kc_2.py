import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

GA_data = pd.read_excel(r'C:\Users\gduncan\OneDrive - Metro United Way, Inc. (191100)\Desktop\Professional Development\Python\Code_Louisville\data_1_checks\assets\GeneralAssembly.xlsx')

GA_data_by_career = GA_data.groupby('Which career path did you choose with General Assembly?', as_index=False)['Respondent ID'].nunique()

print(GA_data_by_career)

plt.style.use('dark_background')
plt.figure(figsize = (12,6))
plt.bar(GA_data_by_career['Which career path did you choose with General Assembly?'], GA_data_by_career['Respondent ID'])
plt.xlabel('Career Type')
plt.ylabel('Number of Graduates')
plt.title('Careers Chosen by Graduates')
plt.show()