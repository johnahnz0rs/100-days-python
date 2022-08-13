import csv
import pandas

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     for d in data:
#         print(d)
    # for d in data[1:]:
    #     print(int(d[1]))


data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
average_temp = data["temp"].mean()
print(f"average temp: {average_temp}")