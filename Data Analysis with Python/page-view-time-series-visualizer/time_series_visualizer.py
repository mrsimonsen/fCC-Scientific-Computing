import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col='date', parse_dates=True)

# Clean data
df = df[(df['value']>=df['value'].quantile(0.025))&(df['value']<=df['value'].quantile(0.975))]


def draw_line_plot():
	# Draw line plot
	t = "Daily freeCodeCamp Forum Page Views 5/2016-12/2019"
	x = "Date"
	y = "Page Views"
	fig = plt.figure(figsize=(16,9))
	sns.lineplot(data=df,legend=False,palette=['red']).set(xlabel=x,ylabel=y,title=t)
	
	# Save image and return fig (don't change this part)
	fig.savefig('line_plot.png')
	return fig

def draw_bar_plot():
	# Copy and modify data for monthly bar plot
	#average daily views by month, grouped by year
	df_bar = df.groupby([df.index.year,df.index.month_name()])['value'].mean().sort_values(['month'])
	#sort by month
	# Draw bar plot
	ax = df_bar.unstack().plot.bar()
	#set labels
	ax.set(xlabel='Years',ylabel='Average Page Views')
	ax.legend(title='Month')
	#get the figure
	fig = plt.gcf()

	# Save image and return fig (don't change this part)
	fig.savefig('bar_plot.png')
	return fig

def draw_box_plot():
	# Prepare data for box plots (this part is done!)
	df_box = df.copy()
	df_box.reset_index(inplace=True)
	df_box['year'] = [d.year for d in df_box.date]
	df_box['month'] = [d.strftime('%b') for d in df_box.date]

	# Draw box plots (using Seaborn)





	# Save image and return fig (don't change this part)
	fig.savefig('box_plot.png')
	return fig
