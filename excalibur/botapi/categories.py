import pandas as pd

df = pd.read_csv("C:\\Users\\Ananya\\Desktop\\team-4\\excalibur\\botapi\\cd_categories.csv")

def category(id):
    return str(df.loc[df['id'] == id]['title'])
