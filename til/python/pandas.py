import pandas as pd

# read_csv
df = pd.read_csv("data/test.csv")

# read_excel (required:$ pip install openpyxl)
df = pd.read_excel("data/test.xlsx", engine='openpyxl', sheet_name=0)
df2 = pd.read_excel("data/test.xlsx", engine='openpyxl', sheet_name=1)

# write excel
output_path = f'data/output.xlsx'
with pd.ExcelWriter(output_path) as writer:
    df.to_excel(writer, sheet_name='物件情報', index=False)
    df2.to_excel(writer, sheet_name='部屋情報', index=False)
