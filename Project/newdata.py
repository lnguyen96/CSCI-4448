import pandas as pd
import numpy as numpy

file = r'database.csv'
fields = ['Vehicle ID', 'Year', 'Make', 'Model', 'Engine Cylinders', 'Fuel Type 1', 'Combined MPG (FT1)', 'Annual Fuel Cost (FT1)']
df = pd.read_csv(file, usecols = fields)
export_csv = df[df.Year >= 2009].to_csv(r'export.csv', index = None, header = True)