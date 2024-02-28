import pandas as pd 

df = pd.read_csv("dairyonly.csv")

df = df[["FF Food description","SR Food description", "FF_Component" , "SR_Component", "SR Mean per 100g", "FF Mean per 100g"]]

df['Mean Difference'] = df['SR Mean per 100g'] - df['FF Mean per 100g']

print(df)


