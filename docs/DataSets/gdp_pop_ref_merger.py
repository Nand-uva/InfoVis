import pandas as pd

# Load the datasets
gdp_per_capita = pd.read_csv('european_countries_gdp_per_capita.csv')
population = pd.read_csv('european_population.csv')
refugee_data = pd.read_csv('UN_European_Countries_Refugee_Data.csv')

# Extracting the relevant years
gdp_years = set(map(int, gdp_per_capita.columns[2:-1]))
pop_years = set(int(col.split()[0]) for col in population.columns[5:] if 'Population' in col and col.split()[0].isdigit())
refugee_years = set(refugee_data['Year'].unique())

# Finding the most recent common year
common_years = gdp_years.intersection(pop_years).intersection(refugee_years)
most_recent_year = max(common_years)

# Extracting data for the most recent common year (2020)
gdp_2020 = gdp_per_capita[['Country Name', '2020']].rename(columns={'Country Name': 'Country', '2020': 'GDP per Capita 2020'})
population_2020 = population[['Country/Territory', '2020 Population']].rename(columns={'Country/Territory': 'Country', '2020 Population': 'Population 2020'})
refugees_2020 = refugee_data[refugee_data['Year'] == 2020][['Country of asylum', 'Refugees under UNHCR\'s mandate']].rename(columns={'Country of asylum': 'Country', 'Refugees under UNHCR\'s mandate': 'Refugees 2020'})

# Aggregating refugee data by country
refugees_2020 = refugees_2020.groupby('Country').sum().reset_index()

# Merging the datasets on the "Country" column
merged_data = gdp_2020.merge(population_2020, on='Country', how='inner')
merged_data = merged_data.merge(refugees_2020, on='Country', how='inner')

# Sorting the merged dataset by the "Country" column
merged_data_sorted = merged_data.sort_values(by='Country')

# Saving the merged dataset to a new CSV file
merged_data_sorted.to_csv('gdp_pop_ref_2020.csv', index=False)
