import pandas as pd

def xlsx_to_csv(xlsx_file, csv_file):
    df = pd.read_excel(xlsx_file)
    
    df.to_csv(csv_file, index=False)
    print(f"Conversion terminée : {csv_file}")

xlsx_file = 'Online Retail.xlsx'
csv_file = 'sales.csv'

xlsx_to_csv(xlsx_file, csv_file)
