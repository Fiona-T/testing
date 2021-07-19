import pandas as pd
import numpy as np
# import seaborn as sns
import matplotlib.pyplot as plt
from uniplot import plot
print('Modules are imported.')

corona_dataset_csv = pd.read_csv("Datasets/covid19_Confirmed_dataset.csv")
# imports the dataset file
corona_dataset_csv.head()
# returns the first five rows of the dataset
print(corona_dataset_csv.head())

print(corona_dataset_csv.shape)
# returns the rows and columns in a tuple e.g. (266, 104)

df = corona_dataset_csv.drop(["Lat", "Long"], axis=1, inplace=True)
# without inplace=True, it creates a copy without those columns

corona_dataset_aggregated = corona_dataset_csv.groupby("Country/Region").sum()
# adds up the rows by this column - as there were multiple rows by country
# this is returned in a new dataframe, now the country/region is the index
print(corona_dataset_aggregated.shape)
# now returns 187 rows and 100 columns
print(corona_dataset_aggregated.loc["China"])
# gets the data from that row

# corona_dataset_aggregated.loc["China"].plot()
# # shows a graph with the data plotted - matplotlibs
# corona_dataset_aggregated.loc["Italy"].plot()
# plt.legend()
# # now shows the graph with two countries on it and a legend - matplotlibs
# corona_dataset_aggregated.loc["China"][:3].plot()
# # gets the first three columns from the start - matplotlibs

plot(ys=corona_dataset_aggregated.loc["China"])
# using uniplot terminal graph, China figures
plot(ys=corona_dataset_aggregated.loc["Italy"])
# using uniplot terminal graph, Italy figures

x = corona_dataset_aggregated.loc["China"]
y = corona_dataset_aggregated.loc["Italy"]
plot(ys=[x, y])
# plot the two series on a single graph together

corona_dataset_aggregated.loc["China"].diff().plot()
# shows the difference from previous column, so new cases per day, plotted

corona_dataset_aggregated.loc["China"].diff().max()
# gets the max amount per day i.e. the max of all the diffs

countries = list(corona_dataset_aggregated.index)
# this gets the index from the dataframe - the index is the country now
# And casts it to a list
# empty list to add the max infection rates to
max_infection_rates = []
# for loop to get the max infection rate for each country
# and append it to the list
for c in countries:
    max_infection_rates.append(corona_dataset_aggregated.loc[c].diff().max())
print(max_infection_rates)
# then print them to see
corona_dataset_aggregated["max_infection_rate"] = max_infection_rates
# adds a new column to the dataset called max_infection_rate,
# using the data from list
print(corona_dataset_aggregated.head())
# this now shows the top of the file, with the new column added

corona_data = pd.DataFrame(corona_dataset_aggregated["max_infection_rate"])
# gives a new dataframe with only the max infection rate column

happiness_report_csv = pd.read_csv("Datasets/worldwide_happiness_report.csv")
print(happiness_report_csv.head())
# import the new file as before and show the first five rowws

useless_columns = ["Overall rank", "Score", "Generosity", "Perceptions of corruption"]
# these are the columns that are not needed
happiness_report_csv.drop(useless_columns, axis=1, inplace=True)
# drop these columns and make the change in the exisitng dataset,
# don't create a new one

happiness_report_csv.set_index("Country or region", inplace=True)
# to make the Country column the index instead of 0,1,2 etc

print(corona_data.shape)
# 187, 1 - 187 rows
print(happiness_report_csv.shape)
# 156,4  - 156 rows

data = corona_data.join(happiness_report_csv, how="inner")
# joins the two together, inner join
print(data.shape)
# now 143 rows and 5 cols

print(data.corr())
# gives a correlation matrix between the different columns in the file

a = data["GDP per capita"]
b = data["max_infection_rate"]
plot(ys=[a, np.log(b)])
