import openpyxl
import pandas as pd

# Get user input
level = input('Which level do you want to convert? ')

# Read CSV file dynamically based on level
df = pd.read_csv(f"level-{level}.csv")

# Calculate percent abundances
percent_abundances = df.iloc[:, 1:].div(df.iloc[:, 1:].sum(axis=1), axis=0) * 100
percent_abundances.insert(0, 'Sample_id', df.iloc[:, 0])

# Transpose the dataframe
trans_df = percent_abundances.T

# Save the percent abundances and transposed dataframe to CSV
percent_abundances.to_csv(f"level-{level}.csv", index=False)
trans_df.to_csv(f'percent_abundance_level_{level}.csv', index=True, header=False)

# Write the percent abundance data to an Excel file
writer = pd.ExcelWriter(f'Excel_file_level_{level}.xlsx', engine='openpyxl')
percent_abundances.to_excel(writer, sheet_name='Percent Abundances', index=False)

# Save and close the Excel writer
writer.close()
