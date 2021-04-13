import pandas as pd
import numpy as np 

def compiled_data():
    compiled_clean = pd.read_csv('SBA_fix.csv')
    # compiled_clean.drop(columns = 'Unnamed: 0', axis = 1, inplace = True)
    # compiled_clean = compiled_clean.sort_values('Date')
    return compiled_clean