index_pod = 0
count = 0
counts = []
for let in need_str:
    if let != pod[index_pod]:
        count += 1
        if let != pod[0]:
            index_pod = 0
    elif not index_pod:
        index_pod += 1
        count += 1
    elif index_pod:
        index_pod = 0
        counts += [count]
        count = 1
counts += [count]
print(max(counts))


import json
import requests
import csv

with open('migration.json') as file:
    data = json.load(file)

запись в csv файл

with open('files/квадраты.csv', 'w', newline='') as csvfile:
    writer = csv.writer(
        csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in range(10):
        writer.writerow([i, i ** 2, "Квадрат числа %d равен %d" % (i, i ** 2)])
