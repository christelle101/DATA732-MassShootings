import pandas as pd
import csv
import json

#reading the csv file
df = pd.read_csv("dataset.csv")
#print(df)

#we choose the keep only the interesting columns
keep_columns = ["case", "location", "date", "fatalities", "injured", "total_victims", "age_of_shooter", "prior_signs_mental_health_issues", "weapons_obtained_legally", "latitude", "longitude", "city", "state"]
keep_columns2 = ["case", "location", "date"]
new_f = df[keep_columns]
new_f.to_csv("filtered_dataset.csv", index=False)

#function to convert CSV to JSON
def convert_to_json(csvFilePath, jsonFilePath):

    #create a dictionary
    data = {}

    #open a csv reader called DictReader
    with open(csvFilePath, encoding="utf8") as csvf:
        csvReader = csv.DictReader(csvf)

        #convert each row into a dictionary and add it to the data
        for rows in csvReader:
            key = rows['case']
            data[key] = rows

    #open a json writer and use the json dumps
    with open(jsonFilePath, 'w', encoding="utf8") as jsonf:
        jsonf.write(json.dumps(data, indent=4))

csvFilePath = r'filtered_dataset.csv'
jsonFilePath = r'USdata.json'

convert_to_json(csvFilePath, jsonFilePath)