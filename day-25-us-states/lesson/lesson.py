# data = []

# with open("weather_data.csv") as file:
#     data = file.readlines()

# print(data)

# import csv

# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for i, row in enumerate(data):
#         if i > 0:
#             temperatures.append(int(row[1]))

# print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)

temp_list = data["temp"].to_list()
print(temp_list)

average = sum(temp_list) / len(temp_list)
print(average)

print(f"Average: {data["temp"].mean()}, Max temperature: {data["temp"].max()}")
print(f"Highest temperature data:\n{data[data["temp"] == data["temp"].max()]}")


monday_temp = data[data.day == "Monday"]
monday_temp = monday_temp["temp"] * 9.0 / 5 + 32
print(f"Monday temperature in Celcius: {monday_temp}")

data_dice = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dice)
data.to_csv("new_data.csv")