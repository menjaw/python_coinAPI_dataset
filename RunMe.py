import pandas as pd
import webget as wg

url = "https://github.com/PeterL93/PythonProject/raw/master/trades_march_to_april_2018.csv"

wg.download(url)

asDataFrame = pd.read_csv('trades_march_to_april_2018.csv', sep=';')

pd.DataFrame(asDataFrame)


#      Question 1
maxVolume = max(asDataFrame["size"])

print("\t\t Question 1\n")
print("The transaction with the highest volume is: " + str(maxVolume))

#      Question 2
count = {}

for row in asDataFrame["time_exchange"]:
        firstSplit = row.split(':')
        secondSplit = firstSplit[0].split('T')

        count.setdefault(secondSplit[1], 0)
        count[secondSplit[1]] += 1

add = 0
sum = 0

for k, v in count.items():
    add += 1
    sum += v

print("\t\tQuestion 2\n")
print("The average number of transactions per hour is: " + str(int(sum/add)))

#      Question 3
buySell = {}

for idx in asDataFrame['taker_side']:
    buySell.setdefault(idx,0)
    buySell[idx] += 1


print("\t\tQuestion 3\n")
print("Most favourite was: "+ str(max(buySell, key=buySell.get)) + " with " + str(max(buySell.values())))
