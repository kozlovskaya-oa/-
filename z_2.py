import csv
import json

filename = input()
res = []

with open(filename, mode="r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=".")
    data = sorted(reader, key=lambda x: (x[2], x[1]))
    print(data)

for el in data:
    if el[0].isdigit():
        dic = {"city": el[2],
               "ship": el[1]}
        res.append(dic)

with open("late.json", mode="w", encoding="utf-8") as f:
    json.dump(res, f)