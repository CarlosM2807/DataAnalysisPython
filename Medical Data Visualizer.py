import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
# Las alturas al cuadrado en metros
altura = (df['height']/100) ** 2
# Pesos
peso = df["weight"]

# ICM
sobrepeso = peso/altura

# Hallo lpongo 1 si es > 25, y 0 si es lo contrario

df['overweight'] = (sobrepeso > 25).astype(int)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.

df["cholesterol"] = (df["cholesterol"] > 1).astype(int)
df["gluc"] = (df["gluc"] > 1).astype(int)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.

    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.

     # Agrupo por cardio / variable / vlor
    # Abajo renombro
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index()
    df_cat = df_cat.rename(columns={0: 'total'})
    
    # Draw the catplot with 'sns.catplot()'

    grafico = sns.catplot(x = "variable", y= "total", hue = "value" , data = df_cat, kind = "bar", col = "cardio")

    # Get the figure for the output
    fig = grafico.fig


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
  # Limpiamos los datos como dice el enunciado
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) 
  & (df['height'] >= df['height'].quantile(0.025)) 
  & (df['height'] <= df['height'].quantile(0.975)) 
  & (df['weight'] >= df['weight'].quantile(0.025))
  & (df['weight'] <= df['weight'].quantile(0.975))] 

    # Calculate the correlation matrix
  # Creamos la matriz de correlcion con el comando
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
  # Visto en internet --> es una mascara para la mitad superior y que no sea dibujada
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True


    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(10, 9))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask = mask, annot= True,fmt=".1f")


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
