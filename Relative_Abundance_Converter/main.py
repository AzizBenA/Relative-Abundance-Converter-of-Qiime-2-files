import pandas as pd

df = pd.read_csv(r"level-7.csv")

percent_abundances = df.iloc[:, 1:].div(df.iloc[:, 1:].sum(axis=1), axis=0) * 100
percent_abundances.insert(0, 'Sample_id', df.iloc[:, 0])

trans_df = percent_abundances.T
print(trans_df)
df.to_csv(r"C:\Users\Aziz Ben Ammar\Desktop\output\level-7.csv", index=False)
trans_df.to_csv(r'C:\Users\Aziz Ben Ammar\Desktop\output\percent_abundance_7.csv', index=True, header=False)

writer = pd.ExcelWriter('Excel_file_level_7.xlsx')
df_1 = pd.read_csv("percent_abundance_7.csv")
df_1.to_excel(writer, index=False)

writer.close()
