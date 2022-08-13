import csv
import pandas

# TASKS
# 1. find out how many gray, cinnamon, or black squirrels there are, based on primary fur color
# 2. create a squirrel_count.csv -- fur color, count



squirrels = pandas.read_csv("2018-census.csv")


gray_count = len(squirrels[squirrels["Primary Fur Color"] == "Gray"])
cinnamon_count = len(squirrels[squirrels["Primary Fur Color"] == "Cinnamon"])
black_count = len(squirrels[squirrels["Primary Fur Color"] == "Black"])

# print(f"gray {len(gray)}")
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "count": [gray_count, cinnamon_count, black_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")

