
import pandas as pd

csv_file = "/home/squirrel/Documents/INF 550 Dataset/train.000"
df = pd.read_csv(csv_file, index_col=0)
hdf = pd.HDFStore("/home/squirrel/Documents/INF 550 Dataset/small.h5")
hdf['df'] = df
hdf.close()
df.to_pickle("/home/squirrel/Documents/INF 550 Dataset/pickle")
print df