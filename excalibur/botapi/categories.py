import pandas as pd

df = pd.read_csv('./cd_categories.csv')

def category(id):
    return str(df.loc[df['id'] == id]['title'])