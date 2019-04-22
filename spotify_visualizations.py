import csv
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Creates a visualization using Release Year and Average Popularity data
def visualization_1():
    # Reads the CSV file and uses pandas to add missing column headers
    info = pd.read_csv('spotify_calculations_1.csv', header=None)
    info.columns = ['Release Year', 'Average Popularity of Your Top Songs']

    # Uses Seaborn to create and format a scatterplot
    sns.set_palette('pastel')
    # Style code was taken from Seaborn's tutorial
    sns.set_style({'axes.axisbelow': True,
    'axes.edgecolor': '.8',
    'axes.facecolor': 'green',
    'axes.grid': True,
    'axes.labelcolor': 'white',
    'axes.spines.bottom': True,
    'axes.spines.left': True,
    'axes.spines.right': True,
    'axes.spines.top': True,
    'figure.facecolor': 'green',
    'font.family': ['sans-serif'],
    'font.sans-serif': ['Arial',
    'DejaVu Sans',
    'Liberation Sans',
    'Bitstream Vera Sans',
    'sans-serif'],
    'grid.color': 'white',
    'grid.linestyle': '-',
    'image.cmap': 'rocket',
    'lines.solid_capstyle': 'round',
    'patch.edgecolor': 'white',
    'patch.force_edgecolor': True,
    'text.color': 'white',
    'xtick.bottom': False,
    'xtick.color': 'white',
    'xtick.direction': 'out',
    'xtick.top': False,
    'ytick.color': 'white',
    'ytick.direction': 'out',
    'ytick.left': False,
    'ytick.right': False})
    
    plt.title('Spotify Data Visualization #1')
    sns.regplot(x='Release Year', y='Average Popularity of Your Top Songs', data=info, color='white', line_kws={"color":"white","alpha":0.7,"lw":5})
    plt.show()

# Creates a visualization for Track Number and Average Popularity 
# This function WILL NOT RUN until the first visualization has been exited out of!
def visualization_2():
    # Reads the CSV file and uses pandas to add missing column headers
    info2 = pd.read_csv('spotify_calculations_2.csv', header=None)
    info2.columns = ['Track Number in Album', 'Average Popularity of Your Top Songs']

    # Uses Seaborn to create and format another scatterplot
    sns.set_palette('pastel')
    sns.set_style({'axes.axisbelow': True,
    'axes.edgecolor': '.8',
    'axes.facecolor': 'lightgreen',
    'axes.grid': True,
    'axes.labelcolor': 'black',
    'axes.spines.bottom': True,
    'axes.spines.left': True,
    'axes.spines.right': True,
    'axes.spines.top': True,
    'figure.facecolor': 'lightgreen',
    'font.family': ['sans-serif'],
    'font.sans-serif': ['Arial',
    'DejaVu Sans',
    'Liberation Sans',
    'Bitstream Vera Sans',
    'sans-serif'],
    'grid.color': 'black',
    'grid.linestyle': '-',
    'image.cmap': 'rocket',
    'lines.solid_capstyle': 'round',
    'patch.edgecolor': 'black',
    'patch.force_edgecolor': True,
    'text.color': 'black',
    'xtick.bottom': False,
    'xtick.color': 'black',
    'xtick.direction': 'out',
    'xtick.top': False,
    'ytick.color': 'black',
    'ytick.direction': 'out',
    'ytick.left': False,
    'ytick.right': False})
    
    plt.title('Spotify Data Visualization #2')
    sns.regplot(x='Track Number in Album', y='Average Popularity of Your Top Songs', data=info2, color='black', line_kws={"color":"black","alpha":0.7,"lw":5})
    plt.show()

# Call functions to create visualizations
visualization_1()
visualization_2()
