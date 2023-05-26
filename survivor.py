'''
===================================================================================================
DESCRIPTION   : Analyze Survivor Contestant Stats 
AUTHOR        : Zack Wixom
DATE UPDATED  : 2023-05-05
VERSION       : 0.01
===================================================================================================
'''
import pandas as pd
import numpy as np
from anonymizedf.anonymizedf import anonymize
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

'''
Import Data
'''
survivors = pd.read_csv('data/survivor_data_contains_spoilers.csv')

'''
Anonymize Contestants
'''

# Create the Fake Contestant Names
anon = anonymize(survivors)
anon.fake_names('contestant')
anon.fake_ids('PID')
anon.fake_categories('Sex')

# Create a "Key"
dfKey = survivors[['contestant', 'Fake_contestant', 'PID', 'Fake_PID', 'Sex', 'Fake_Sex']]
dfKey.to_csv('data/key.csv')

# Clean up dataset
survivors = survivors.assign(contestant = survivors['Fake_contestant'], PID = survivors['Fake_PID'], Sex = survivors['Fake_Sex'])
survivors = survivors.drop(columns = ['Fake_contestant', 'Fake_PID', 'Fake_Sex'])

# Shuffle data
survivors = survivors.sort_values('PID')

'''
Exploratory Data Analysis
'''

# Look at data and data types
survivors.head()
survivors.describe()
survivors.dtypes

# Convert date variables
survivors['Day 1 Filming date'] = pd.to_datetime(survivors['Day 1 Filming date'])
survivors['Birthday'] = pd.to_datetime(survivors['Birthday'])

# Drop empty column
survivors = survivors.drop(columns= ['Unnamed: 51'])

# Save cleaned dataset
survivors.to_csv('data/survivor.csv')

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
    y = 'median_age',
    title = 'Mean Age of Contestant Placement'
    ).add_trace(go.Scatter(
        # x = placement_mean_age.Finish,
        y = placement_mean_age.num_contestants, 
        mode = 'lines',
        name = 'n Contestants'
    ))
fig.show()


# Histogram of Ages in Survivors
fig = px.histogram(
    survivors, 
    x = 'Age'
    )
fig.show()


