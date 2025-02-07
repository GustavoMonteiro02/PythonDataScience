import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Load the data
df = pd.read_csv('medical_examination.csv')

# 2. Add 'overweight' column
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# 3. Normalize data by making 0 always good and 1 always bad
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

# 4. Function to draw the categorical plot
def draw_cat_plot():
    # 5. Create DataFrame for catplot
    df_cat = pd.melt(df, id_vars='cardio', value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 6. Group and reformat the data to split it by 'cardio'
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # 7. Draw the catplot
    fig = sns.catplot(
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        data=df_cat,
        kind='bar',
        height=4,
        aspect=1
    )

    # 8. Set the y-axis label to 'total'
    fig.set_axis_labels("variable", "total")

    # 9. Save the plot
    fig.savefig('catplot.png')

    # 10. Return the figure object
    return fig.fig

# 11. Function to draw the heatmap
def draw_heat_map():
    # 12. Clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) & 
        (df['height'] >= df['height'].quantile(0.025)) & 
        (df['height'] <= df['height'].quantile(0.975)) & 
        (df['weight'] >= df['weight'].quantile(0.025)) & 
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 13. Calculate the correlation matrix
    corr = df_heat.corr()

    # 14. Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 15. Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(10, 8))

    # 16. Draw the heatmap
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt='.1f',
        cmap='coolwarm',
        square=True,
        cbar_kws={"shrink": .8},
        ax=ax
    )

    # 17. Save the heatmap
    fig.savefig('heatmap.png')

    # 18. Return the figure object
    return fig