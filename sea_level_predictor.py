import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(data = df, x = 'Year', y = 'CSIRO Adjusted Sea Level')

    # Create first line of best fit
    lobf = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_vals = range(df['Year'].min(),2051)
    y_vals = lobf.intercept + lobf.slope * x_vals
    ax.plot(x_vals, y_vals,'r', label ='fitted line')

    # Create second line of best fit
    df_filtered = df[df['Year'] >= 2000]
    lobf2 = linregress(df_filtered['Year'], df_filtered['CSIRO Adjusted Sea Level'])
    x_vals2 = range(df_filtered['Year'].min(),2051)
    y_vals2 = lobf2.intercept + lobf2.slope * x_vals2
    ax.plot(x_vals2, y_vals2,'r', label ='fitted line')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()