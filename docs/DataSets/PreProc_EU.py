import pandas as pd

# Load the data
file_path = 'UN_World_Refugee Data.csv'
data = pd.read_csv(file_path)

# Filter the dataset for European countries excluding Russia using ISO codes
european_countries_iso = [
    'ALB', 'AUT', 'BLR', 'BEL', 'BIH', 'BGR', 'HRV', 'CYP', 'CZE', 'DNK', 'EST', 
    'FIN', 'FRA', 'DEU', 'GRC', 'HUN', 'ISL', 'IRL', 'ITA', 'LVA', 'LIE', 'LTU', 
    'LUX', 'MLT', 'MDA', 'MCO', 'MNE', 'NLD', 'MKD', 'NOR', 'POL', 'PRT', 'ROU', 
    'SRB', 'SVK', 'SVN', 'ESP', 'SWE', 'CHE', 'TUR', 'UKR', 'GBR'
]

# Filter the dataset
european_data = data[data['Country of asylum (ISO)'].isin(european_countries_iso)]

# Save the filtered data to a new CSV file
output_file_path = 'UN_European_Countries_Refugee_Data.csv'
european_data.to_csv(output_file_path, index=False)
