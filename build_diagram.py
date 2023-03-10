import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import csv

df = pd.read_csv('number19_python_diagram_adaption.csv')

sns.boxplot(y='value', x='date', data=df, palette='colorblind', hue='type')
plt.show()
