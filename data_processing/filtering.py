import pandas as pd

df=pd.read_csv('dataset.csv')

#print(df.columns.get_loc("weapon_type"))
#print(df.columns.get_loc("race"))
#print(df.columns.get_loc("gender"))

df=df.drop(df.columns[[10,12,13,14,15,16,18,19,22,23]], axis='columns')

df=df.rename(columns = {'location.1': 'setting'})

df[['city','state']] = df.location.str.split(",",expand=True,)
df['city'] = df.city.str.strip()
df['state'] = df.state.str.strip()

#print(df)

df.to_csv('filtered_dataset.csv')

"""
    Processing on the age column
"""
dfAge = df[df['age_of_shooter']!='-']
dfAge["age_of_shooter"] = pd.to_numeric(dfAge["age_of_shooter"])
valuesList = []

num21 = len(dfAge.loc[(dfAge['age_of_shooter']<=21),:])
valuesList.append(num21)

num2230=len(dfAge.loc[(dfAge['age_of_shooter']>=22) & (dfAge['age_of_shooter']<=30),:])
valuesList.append(num2230)

num3140=len(dfAge.loc[(dfAge['age_of_shooter']>=31) & (dfAge['age_of_shooter']<=40),:])
valuesList.append(num3140)

num4150=len(dfAge.loc[(dfAge['age_of_shooter']>=41) & (dfAge['age_of_shooter']<=50),:])
valuesList.append(num4150)

num5160=len(dfAge.loc[(dfAge['age_of_shooter']>=51) & (dfAge['age_of_shooter']<=60),:])
valuesList.append(num5160)

num61 = len(dfAge.loc[(dfAge['age_of_shooter']>=61),:])
valuesList.append(num61)

#print(valuesList)

df2 = pd.DataFrame(columns=['category','value'])
df2['category']=['<21','22-30','31-40','41-50','51-60','>61']
df2['value'] = valuesList

df2.to_csv('age_filtered.csv', index = False)

"""
Creation of a new dataset with age repartition, total victims and mental health status
"""
listVictims = []

victim21 = dfAge.query('age_of_shooter <= 21')
victim21_v = victim21['total_victims']
victims21 = victim21_v.sum(axis = 0, skipna = True)
listVictims.append(victims21)

victim2230 = dfAge.query('age_of_shooter >= 22 & age_of_shooter <= 30')
victim2230_v = victim2230['total_victims']
victims2230 = victim2230_v.sum(axis = 0, skipna = True)
listVictims.append(victims2230)

victim3140 = dfAge.query('age_of_shooter >= 31 & age_of_shooter <= 40')
victim3140_v = victim3140['total_victims']
victims3140 = victim3140_v.sum(axis = 0, skipna = True)
listVictims.append(victims3140)

victim4150 = dfAge.query('age_of_shooter >= 41 & age_of_shooter <= 50')
victim4150_v = victim4150['total_victims']
victims4150 = victim4150_v.sum(axis = 0, skipna = True)
listVictims.append(victims4150)

victim5160 = dfAge.query('age_of_shooter >= 51 & age_of_shooter <= 60')
victim5160_v = victim5160['total_victims']
victims5160 = victim5160_v.sum(axis = 0, skipna = True)
listVictims.append(victims4150)

victim61 = dfAge.query('age_of_shooter >= 61')
victim61_v = victim61['total_victims']
victims61 = victim61_v.sum(axis = 0, skipna = True)
listVictims.append(victims61)

listMentals = []

mental21 = dfAge.query(
'age_of_shooter <= 21 & (prior_signs_mental_health_issues == "yes" or prior_signs_mental_health_issues == "Yes")')
mental21_v = mental21['total_victims']
mentals21 = mental21_v.sum(axis = 0, skipna = True)
listMentals.append(mentals21)

mental2230 = dfAge.query(
'age_of_shooter <= 22 & age_of_shooter <= 30 & (prior_signs_mental_health_issues == "yes" or prior_signs_mental_health_issues == "Yes")')
mental2230_v = mental2230['total_victims']
mentals2230 = mental2230_v.sum(axis = 0, skipna = True)
listMentals.append(mentals2230)

mental3140 = dfAge.query(
'age_of_shooter <= 31 & age_of_shooter <= 40 & (prior_signs_mental_health_issues == "yes" or prior_signs_mental_health_issues == "Yes")')
mental3140_v = mental3140['total_victims']
mentals3140 = mental3140_v.sum(axis = 0, skipna = True)
listMentals.append(mentals3140)

mental4150 = dfAge.query(
'age_of_shooter <= 41 & age_of_shooter <= 50 & (prior_signs_mental_health_issues == "yes" or prior_signs_mental_health_issues == "Yes")')
mental4150_v = mental4150['total_victims']
mentals4150 = mental4150_v.sum(axis = 0, skipna = True)
listMentals.append(mentals4150)

mental5160 = dfAge.query(
'age_of_shooter <= 51 & age_of_shooter <= 60 & (prior_signs_mental_health_issues == "yes" or prior_signs_mental_health_issues == "Yes")')
mental5160_v = mental5160['total_victims']
mentals5160 = mental5160_v.sum(axis = 0, skipna = True)
listMentals.append(mentals5160)

mental61 = dfAge.query(
'age_of_shooter >= 61 & (prior_signs_mental_health_issues == "yes" or prior_signs_mental_health_issues == "Yes")')
mental61_v = mental61['total_victims']
mentals61 = mental61_v.sum(axis = 0, skipna = True)
listMentals.append(mentals61)

df3 = pd.DataFrame(columns=['category','total_victims'])
df3['category']=['<21','22-30','31-40','41-50','51-60','>61']
df3['total_victims'] = listVictims
df3.to_csv('victims_byAge.csv', index = False)

df4 = pd.DataFrame(columns=['age_category','mentally_ill'])
df4['age_category']=['<21','22-30','31-40','41-50','51-60','>61']
df4['mentally_ill'] = listMentals
df4.to_csv('mentals_byAge.csv', index = False)
