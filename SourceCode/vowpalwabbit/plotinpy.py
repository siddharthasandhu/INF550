import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib
arr1 = []
arr2 = []
for row in open("VwConversionTime.txt"):
    row = row.strip("\n").split("\t")
    arr1.append(row[0])
    rows = row[1].split(":")
    var = 0
    if int(rows[0]) > 0:
        var = int(rows[0])*60
    mins = var + int(rows[1])
    arr2.append(float(mins)/60)
    print mins
    #print datetime.strptime(row[1].split(".")[0], "%H:%M:%S")
#dates = matplotlib.dates.datestr2num(arr2)
plt.xlabel("Data Size")
plt.ylabel("Time in Hours")
plt.grid(True)
plt.plot(arr1,arr2)
plt.show()