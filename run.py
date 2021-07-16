import pandas as pd
import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
print('Modules are imported.')

corona_dataset_csv = pd.read_csv("Datasets/covid19_Confirmed_dataset.csv")
# imports the dataset file
corona_dataset_csv.head()
# returns the first five rows of the dataset
print(corona_dataset_csv.head())

print(corona_dataset_csv.shape)
# returns the rows and columns in a tuple e.g. (266, 104)
