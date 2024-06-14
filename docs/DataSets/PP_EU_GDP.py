import pandas as pd

# Load the CSV file
file_path = 'gdp_per_capita.csv'
df = pd.read_csv(file_path)

# List of European countries
european_countries = [
    'Albania', 'Andorra', 'Austria', 'Belarus', 'Belgium', 'Bosnia and Herzegovina', 
    'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 
    'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Kosovo', 'Latvia', 'Liechtenstein', 
    'Lithuania', 'Luxembourg', 'Malta', 'Moldova', 'Monaco', 'Montenegro', 'Netherlands', 'North Macedonia', 
    'Norway', 'Poland', 'Portugal', 'Romania', 'San Marino', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 
    'Switzerland', 'Turkey', 'Ukraine', 'United Kingdom', 'Vatican City'
]

# Filter the dataframe to only include European countries
european_df = df[df['Country Name'].isin(european_countries)]

# Save the filtered dataframe to a new CSV file
output_file_path = 'european_countries_gdp_per_capita.csv'
european_df.to_csv(output_file_path, index=False)
