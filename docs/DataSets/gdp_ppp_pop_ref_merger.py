import pandas as pd

# Load the datasets
gdp_ppp_per_capita = pd.read_csv('european_countries_gdp_ppp_per_capita.csv')
population = pd.read_csv('european_population.csv')
refugee_data = pd.read_csv('UN_European_Countries_Refugee_Data.csv')

# Ensure we use the correct column for ISO codes
gdp_ppp_per_capita = gdp_ppp_per_capita.rename(columns={'Code': 'ISO_Code'})
population = population.rename(columns={'CCA3': 'ISO_Code'})
refugee_data = refugee_data.rename(columns={'Country of asylum (ISO)': 'ISO_Code'})

# Extracting the relevant years
gdp_years = set(map(int, gdp_ppp_per_capita.columns[2:-1]))
pop_years = set(int(col.split()[0]) for col in population.columns[5:] if 'Population' in col and col.split()[0].isdigit())
refugee_years = set(refugee_data['Year'].unique())

# Finding the most recent common year
common_years = gdp_years.intersection(pop_years).intersection(refugee_years)
most_recent_year = max(common_years)

# Extracting data for the most recent common year (2020)
gdp_ppp_2020 = gdp_ppp_per_capita[['ISO_Code', '2020']].rename(columns={'2020': 'GDP PPP per Capita 2020'})
population_2020 = population[['ISO_Code', '2020 Population']].rename(columns={'2020 Population': 'Population 2020'})
refugees_2020 = refugee_data[refugee_data['Year'] == 2020][['ISO_Code', 'Refugees under UNHCR\'s mandate']].rename(columns={'Refugees under UNHCR\'s mandate': 'Refugees 2020'})

# Aggregating refugee data by ISO code
refugees_2020 = refugees_2020.groupby('ISO_Code').sum().reset_index()

# Merging the datasets on the "ISO_Code" column
merged_data = gdp_ppp_2020.merge(population_2020, on='ISO_Code', how='inner')
merged_data = merged_data.merge(refugees_2020, on='ISO_Code', how='inner')

# Sorting the merged dataset by the "ISO_Code" column
merged_data_sorted = merged_data.sort_values(by='ISO_Code')

# Saving the merged dataset to a new CSV file
merged_data_sorted.to_csv('GDP_PPP_Per_Capita_Europe.csv', index=False)
