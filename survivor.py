'''
===================================================================================================
DESCRIPTION   : Analyze Survivor Contestant Stats 
AUTHOR(S)     : Zack Wixom
DATE          : 2023-04-21
VERSION       : 0.01
===================================================================================================
'''
import pandas as pd
from anonymizedf.anonymizedf import anonymize

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

