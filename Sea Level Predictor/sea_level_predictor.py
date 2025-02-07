import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], color='blue', label='Data')
    
    # Create first line of best fit (using all data)
    slope_all, intercept_all, _, _, _ = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))
    sea_level_all = slope_all * years_extended + intercept_all
    plt.plot(years_extended, sea_level_all, color='red', label='Best Fit Line (All Data)')
    
    # Create second line of best fit (using data from 2000 onwards)
    data_2000 = data[data['Year'] >= 2000]
    slope_2000, intercept_2000, _, _, _ = linregress(data_2000['Year'], data_2000['CSIRO Adjusted Sea Level'])
    years_2000_extended = pd.Series(range(2000, 2051))
    sea_level_2000 = slope_2000 * years_2000_extended + intercept_2000
    plt.plot(years_2000_extended, sea_level_2000, color='green', label='Best Fit Line (2000 Onwards)')
    
    # Add labels, title, and legend
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()