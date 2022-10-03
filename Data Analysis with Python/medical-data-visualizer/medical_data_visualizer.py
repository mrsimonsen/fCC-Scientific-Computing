import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv', index_col=0)

# Add 'overweight' column
df['overweight'] = ((df['weight']/(df['height']/100)**2)>25).astype(int)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# Draw Categorical Plot
def draw_cat_plot():
	# Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
	df_cat = df.melt(id_vars=['cardio'],value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
	# Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
	groups = df_cat.groupby(['cardio','variable','value']).size().reset_index()
	index = groups.columns.tolist()
	index[-1] = 'total'
	groups.columns = index
	# Draw the catplot with 'sns.catplot()'
	# Get the figure for the output
	fig = sns.catplot(data=groups, x='variable', y='total', col='cardio',hue='value',kind='bar')


	# Do not modify the next two lines
	fig.savefig('catplot.png')
	return fig

# Draw Heat Map
def draw_heat_map():
	# Clean the data
	df_heat = None

	# Calculate the correlation matrix
	corr = None

	# Generate a mask for the upper triangle
	mask = None



	# Set up the matplotlib figure
	fig, ax = None

	# Draw the heatmap with 'sns.heatmap()'



	# Do not modify the next two lines
	fig.savefig('heatmap.png')
	return fig
