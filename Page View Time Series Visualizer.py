import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv",parse_dates = True, index_col = 'date', infer_datetime_format = True)

# Clean data
# Intercuartil 0.025
# Los primeros
primeros = df["value"] >= df["value"].quantile(0.025)
# Los ultimos
ultimos = df["value"] <= df["value"].quantile(0.975)

df = df.loc[(primeros & ultimos)]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(25, 20), dpi=100)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    plt.plot(df.index.values, df.value, color = 'red')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df['month'] = pd.DatetimeIndex(df.index.values).month_name()
    df['year'] = pd.DatetimeIndex(df.index.values).year

    df_bar = df.groupby(['year', 'month'], as_index = False, sort = False)['value'].mean()

    # Draw bar plot
    Months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    fig, ax = plt.subplots(figsize = (12, 12))
    sns.barplot(data = df_bar, x = 'year', y = 'value', hue = 'month', hue_order = Months, palette = 'husl')
    plt.legend(loc = 'upper left', title = 'Months')
    ax.set_ylabel('Average Page Views')
    ax.set_xlabel('Years')

    # Save image and return fig
    fig.savefig('bar_plot.png')
    return fig

# draw_box_plot() that creates two sets of boxplots. The first show the distribution of page views over each year.
# The second show the distribution of page views over the months.
def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    Months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    fig, ax = plt.subplots(ncols = 2, figsize = (20, 10))

    sns.boxplot(data = df_box, x = 'year', y = 'value', ax = ax[0])
    ax[0].set_title('Year-wise Box Plot (Trend)')
    ax[0].set_ylabel('Page Views')
    ax[0].set_xlabel('Year')

    sns.boxplot(data = df_box, x = 'month', y = 'value', order = Months, ax = ax[1])
    ax[1].set_title('Month-wise Box Plot (Seasonality)')
    ax[1].set_ylabel('Page Views')
    ax[1].set_xlabel('Month')

    # Save image and return fig
    fig.savefig('box_plot.png')
    return fig