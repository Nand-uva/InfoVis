import pandas as pd

# Load the CSV file
file_path = 'gdp_per_capita.csv'
df = pd.read_csv(file_path)

# List of ISO codes for European countries
european_countries_iso = [
    'ALB', 'AUT', 'BLR', 'BEL', 'BIH', 'BGR', 'HRV', 'CYP', 'CZE', 'DNK', 'EST', 
    'FIN', 'FRA', 'DEU', 'GRC', 'HUN', 'ISL', 'IRL', 'ITA', 'LVA', 'LIE', 'LTU', 
    'LUX', 'MLT', 'MDA', 'MCO', 'MNE', 'NLD', 'MKD', 'NOR', 'POL', 'PRT', 'ROU', 
    'SRB', 'SVK', 'SVN', 'ESP', 'SWE', 'CHE', 'TUR', 'UKR', 'GBR'
]

# Filter the dataframe to only include European countries using the 'Code' column for ISO codes
european_df = df[df['Code'].isin(european_countries_iso)]

# Save the filtered dataframe to a new CSV file
output_file_path = 'european_countries_gdp_per_capita.csv'
european_df.to_csv(output_file_path, index=False)
