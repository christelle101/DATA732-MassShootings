import pandas as pd

df=pd.read_csv('dataset.csv')

print(df.columns.get_loc("weapon_type"))
print(df.columns.get_loc("race"))
print(df.columns.get_loc("gender"))

df=df.drop(df.columns[[10,12,13,14,15,16,18,19,22,23]], axis='columns')

df=df.rename(columns = {'location.1': 'setting'})

df[['city','state']] = df.location.str.split(",",expand=True,)
df['city']=df.city.str.strip()
df['state']=df.state.str.strip()

print(df)

df.to_csv('filtered_dataset.csv')