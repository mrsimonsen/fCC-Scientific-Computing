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
	historic_years = range(1880, 2051)
	historic_predictions = [line1.intercept + line1.slope*year for year in historic_years]
	plt.plot(historic_years, historic_predictions, color='red')

	# Create second line of best fit
	recent_data = df[df['Year']>=2000]
	recent_years = range(2000,2051)
	line2 = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
	recent_predictions = [line2.intercept + line2.slope*year for year in recent_years]
	plt.plot(recent_years, recent_predictions, color='blue')

	# Add labels and title
	plt.xlabel("Year")
	plt.ylabel("Sea Level (inches)")
	plt.title("Rise in Sea Level")

	# Save plot and return data for testing (DO NOT MODIFY)
	plt.savefig('sea_level_plot.png')
	return plt.gca()