
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df.set_index('date', inplace=True)

# Clean dataClean the data by filtering out days when the page views were in the 
# top 2.5% of the dataset or bottom 2.5% of the dataset.
df = df[(df['value']>df['value'].quantile(0.025)) & (df['value']<df['value'].quantile(0.975))]

#Create a draw_line_plot function that uses Matplotlib to draw a line chart 
# The title should be Daily freeCodeCamp Forum Page Views 5/2016-12/2019. 
# The label on the x axis should be Date and the label on the y axis should be Page Views.
def draw_line_plot():
    df.plot(color='r', figsize=(15, 5), legend=False)
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    fig=plt.gcf()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

#Create a draw_bar_plot function that draws a bar chart. It should show average daily page views 
# for each month grouped by year. The legend should show month labels and have a title of Months. 
# On the chart, the label on the x axis should be Years and the label on the y axis should be Average Page Views.
def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar=df.copy()
    df_bar.index = pd.to_datetime(df_bar.index)
    df_bar['Year'] = df_bar.index.year
    df_bar['Month'] = df_bar.index.month_name()

    # Pivot the DataFrame to get the right structure for plotting
    df_barpivot = df_bar.pivot_table(values='value', index='Year', columns='Month', aggfunc='mean')
    month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
    df_barpivot = df_barpivot.reindex(columns=month_order)
  

    #make bar plot
    df_barpivot.plot(kind='bar', figsize=(10, 10))
    plt.legend(title='Months')
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    fig=plt.gcf()


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

##reate a draw_box_plot function that uses Seaborn to draw two adjacent box plots similar to "examples/Figure_3.png".
#  These box plots should show how the values are distributed within a given year or month and how it compares over time.
#  The title of the first chart should be Year-wise Box Plot (Trend) and the title of the second chart should be 
# Month-wise Box Plot (Seasonality).  Make sure the month labels on bottom start at Jan and the x and y axis are labeled correctly. 
def draw_box_plot():
    # Prepare data for box plots 
    df_box = df.copy()
    df_box.index = pd.to_datetime(df_box.index)
    df_box['Year'] = df_box.index.year
    df_box['Month'] = df_box.index.strftime('%b')
    
    
    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(nrows=1, ncols=2,figsize=(18, 6))

    # Box plot by Year
    sns.boxplot(x='Year', y='value', data=df_box, ax=axes[0], palette='deep',fliersize=1)
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_ylabel('Page Views')

    # Box plot by Month
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(x='Month', y='value', data=df_box, ax=axes[1], order=month_order,palette='pastel',fliersize=1)
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
