import pandas as pd

# Load the data
file_path = 'United Nations Refugee Data.csv'
data = pd.read_csv(file_path)

# Extracting European countries excluding Russia
european_countries = [
    'Albania', 'Andorra', 'Armenia', 'Austria', 'Azerbaijan', 'Belarus', 'Belgium', 'Bosnia and Herzegovina', 
    'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Georgia', 
    'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Kazakhstan', 'Kosovo', 'Latvia', 'Liechtenstein', 
    'Lithuania', 'Luxembourg', 'Malta', 'Moldova', 'Monaco', 'Montenegro', 'Netherlands', 'North Macedonia', 
    'Norway', 'Poland', 'Portugal', 'Romania', 'San Marino', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 
    'Switzerland', 'Turkey', 'Ukraine', 'United Kingdom', 'Vatican City'
]

# Filter the dataset for European countries excluding Russia
european_data = data[data['Country of asylum'].isin(european_countries)]

# Save the filtered data to a new CSV file
output_file_path = 'European_Countries_Refugee_Data.csv'
european_data.to_csv(output_file_path, index=False)
