import pandas as pd


dataframe = pd.read_csv("Part2/Titanic.csv")

dataframe.dropna(axis=0, how='any', inplace=True)
delete_list = []
ignore_delete = ['Sex', 'Embarked']
for column in dataframe:
    try:
        float(dataframe[column][1])
    except ValueError:
        if column in ignore_delete:
            continue
        delete_list.append(column)
delete_list.append('PassengerId')
dataframe.drop(delete_list, axis=1, inplace=True)

convert_sex = {'male': 0, 'female': 1}
convert_embarked = {'C': 1, 'Q': 2, 'S': 3}

for key in convert_sex:
    dataframe.replace(key, convert_sex[key], inplace=True)
for key in convert_embarked:
    dataframe.replace(key, convert_embarked[key], inplace=True)

print(dataframe)