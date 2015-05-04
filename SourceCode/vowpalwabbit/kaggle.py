__author__ = 'Siddhartha'

import math

def zygmoid(x):
	#I know it's a common Sigmoid feature, but that's why I probably found
	#it on FastML too: https://github.com/zygmuntz/kaggle-stackoverflow/blob/master/sigmoid_mc.py
	return 1 / (1 + math.exp(-x))

with open("/home/squirrel/Documents/INF 550 Dataset/submission.csv","wb") as outfile:
	outfile.write("id,click\n")
	for line in open("/home/squirrel/Documents/INF 550 Dataset/avazu.preds.txt"):
		row = line.strip().split(" ")
		outfile.write("%s,%f\n"%(row[1],zygmoid(float(row[0]))))
