import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
	# Read data from file
	df = pd.read_csv('epa-sea-level.csv')

	# Create scatter plot
	plt.scatter(x=df['Year'],y=df['CSIRO Adjusted Sea Level'])
	

	# Create first line of best fit
	line1 = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
	future_years = range(1880, 2051)
	future_predictions = [line1.intercept + line1.slope*year for year in future_years]
	plt.plot(future_years, future_predictions, color='red')

	# Create second line of best fit


	# Add labels and title


	# Save plot and return data for testing (DO NOT MODIFY)
	plt.savefig('sea_level_plot.png')
	return plt.gca()