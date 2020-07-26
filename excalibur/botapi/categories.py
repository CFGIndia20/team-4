import pandas as pd

df = pd.read_csv('D:\\programs\\competitions\\JPMC-CFG20\\team-4\\excalibur\\botapi\\cd_categories.csv')

def category(id):
    return str(df.loc[df['id'] == id]['title'])