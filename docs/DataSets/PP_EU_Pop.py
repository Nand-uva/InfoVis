import pandas as pd

# Load the CSV file
file_path = 'world_population.csv'
df = pd.read_csv(file_path)

# List of ISO codes for European countries
european_countries_iso = [
    'ALB', 'AUT', 'BLR', 'BEL', 'BIH', 'BGR', 'HRV', 'CYP', 'CZE', 'DNK', 'EST', 
    'FIN', 'FRA', 'DEU', 'GRC', 'HUN', 'ISL', 'IRL', 'ITA', 'LVA', 'LIE', 'LTU', 
    'LUX', 'MLT', 'MDA', 'MCO', 'MNE', 'NLD', 'MKD', 'NOR', 'POL', 'PRT', 'ROU', 
    'SRB', 'SVK', 'SVN', 'ESP', 'SWE', 'CHE', 'TUR', 'UKR', 'GBR'
]

# Filter the dataframe to only include European countries using the CCA3 column
european_df = df[df['CCA3'].isin(european_countries_iso)]

# Save the filtered dataframe to a new CSV file
output_file_path = 'european_population.csv'
european_df.to_csv(output_file_path, index=False)