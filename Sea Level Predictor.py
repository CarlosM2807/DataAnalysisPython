import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Importo nunpy porque lo necesito 
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    #print(df)

    # Create scatter plot
    anos = df['Year']
    csiro = df["CSIRO Adjusted Sea Level"]
    plt.scatter(anos,csiro)
    
    anomin = anos.min()
    # Create first line of best fit
    primeraLinea = linregress(anos,csiro)
    valorA = np.arange(anomin,2050,1)
    valorY = valorA*primeraLinea.slope + primeraLinea.intercept
    
    # Lo pongo en el plot
    plt.plot(valorA,valorY)

    # Create second line of best fit
    mas2000 = df[df["Year"] >= 2000]
    anos2 = mas2000['Year']
    csiro2 = mas2000["CSIRO Adjusted Sea Level"]

    segundaLinea = linregress(anos2,csiro2)
    valorA2 = np.arange(2000,2050,1)
    valorY2 = valorA2*segundaLinea.slope + segundaLinea.intercept
    
    plt.plot(valorA2,valorY2)
    # Add labels and title
  # Ponemos las etiquetas de titulo y tal
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()