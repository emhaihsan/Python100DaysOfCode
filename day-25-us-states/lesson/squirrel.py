import pandas

data = pandas.read_csv("squirrel_data.csv")

data['Primary Fur Color'] == 'Gray'
gray_squirrels_count = len(data[data['Primary Fur Color'] == 'Gray'])

data['Primary Fur Color'] == 'Cinnamon'
cinnamon_squirrels_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])

data['Primary Fur Color'] == 'Black'
black_squirrels_count = len(data[data['Primary Fur Color'] == 'Black'])

data_dict = pandas.DataFrame({'Fur Color': ['Gray', 'Cinnamon', 'Black'], 'Count': [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]})
data_dict.to_csv('squirrel_count.csv')
