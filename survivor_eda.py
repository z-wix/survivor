'''
===================================================================================================
DESCRIPTION   : Exploratoy Data Analysis for Survivor data
AUTHOR        : Zack Wixom
DATE UPDATED  : 2023-05-05
VERSION       : 0.01
===================================================================================================
'''
import pandas as pd
import numpy as np
import scipy

import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from chart_studio import plotly

'''
Import Data
'''
survivors = pd.read_csv('data/survivor.csv')

'''
===================================================================================================
Exploratory Data Analysis
===================================================================================================
'''

survivors.head()

'''
Exploring Age
'''

# Histogram of Ages in Survivors
fig = px.histogram(
    survivors, 
    x = 'Age'
    )
fig.show()

# Stats for Age
age_mean = np.mean(survivors['Age'])
age_sd = np.std(survivors['Age'])

print(f'Age mean: {age_mean} and standard deviation: {age_sd}')

# Grouping by Placement and Age
placement_mean_age = survivors.groupby('Finish').agg(
    mean_age = ('Age', np.mean),
    median_age = ('Age', np.median),
    num_contestants = ('contestant', np.size)
).reset_index()

# Chart for mean age and num of contestants per placement
fig = px.bar(
    placement_mean_age, 
    x = 'Finish',
    y = 'mean_age',
    title = 'Mean Age of Contestant Placement'
    ).add_trace(go.Scatter(
        # x = placement_mean_age.Finish,
        y = placement_mean_age.num_contestants, 
        mode = 'lines',
        name = 'n Contestants'
    ))
fig.show()


# Grouping by Season and Age
season_mean_age = survivors.groupby('Season').agg(
    mean_age = ('Age', np.mean),
    median_age = ('Age', np.median),
    num_contestants = ('contestant', np.size)
).reset_index()

# Chart for mean age and num of contestants per placement
fig = px.bar(
    season_mean_age, 
    x = 'Season',
    y = 'mean_age',
    title = 'Mean Age of Season'
    ).add_trace(go.Scatter(
        # x = season_mean_age.Finish,
        y = season_mean_age.num_contestants, 
        mode = 'lines',
        name = 'n Contestants'
    ))
fig.show()


# Grouping by Season and Days
season_mean_day = survivors.groupby('Season').agg(
    mean_days = ('Days', np.mean),
    median_days = ('Days', np.median),
    num_contestants = ('contestant', np.size)
).reset_index()

# Chart for mean age and num of contestants per placement
fig = px.bar(
    season_mean_day, 
    x = 'Season',
    y = 'mean_days',
    title = 'Mean Days of Season'
    ).add_trace(go.Scatter(
        # x = season_mean_age.Finish,
        y = season_mean_day.num_contestants, 
        mode = 'lines',
        name = 'n Contestants'
    ))
fig.show()

'''
===================================================================================================
Correlation Analysis
===================================================================================================
'''

import seaborn as sns
import matplotlib.pyplot as plt

numerics = ['int64', 'float64']
survivors_num = survivors.select_dtypes(include= numerics)

survivors[survivors_num.columns].corr()

survivors[survivors_num.columns].corr().style.background_gradient(cmap='vlag')

