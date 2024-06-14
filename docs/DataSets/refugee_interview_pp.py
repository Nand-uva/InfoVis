import pandas as pd

file_path = 'refugee_interview.csv'
data = pd.read_csv(file_path)

filtered_df = data[~data['VAR01'].isin([1, 2])] #1 and 2 are Iraq and Lebanon, these are not in Europe

filtered_file_path = 'refugee_interview_filtered.csv'
filtered_df.to_csv(filtered_file_path, index=False)