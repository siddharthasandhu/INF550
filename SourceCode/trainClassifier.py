__author__ = 'FarhanKhwaja'

from sklearn.externals import joblib
import pandas as pd
import numpy as np
from os import listdir
from os.path import isfile, join
from sklearn import linear_model
from sklearn.preprocessing import OneHotEncoder

'''Training Classifier by reading 500000 data at a time.
Converting the Categorical data to One Hot Encoding, and passing it to the classifier.

Lastly, saving the classifier'''

def trainClass(data,header, cntr, uniqVal):

    train = pd.DataFrame(data=np.asarray(data),columns=header)
    train_class =  np.array(train.click.astype(int))
    header = ['C1' ,'C14', 'banner_pos', 'site_category', 'app_domain', 'device_type', 'device_conn_type']
    train = train[header]

    for classval in np.unique(train_class):
        uniqVal.setdefault('class',[])
        if classval not in uniqVal['class']:
            uniqVal['class'].append(classval)

    for x in header:
        uniqVal.setdefault(x,[])
        for val in np.unique(train[x].ravel()):
            if val not in uniqVal[x]:
                uniqVal[x].append(val)

        for idx, value in enumerate(uniqVal[x]):
            train[x][train[x] == value] = idx

    joblib.dump(uniqVal,'DataChunks/uniqueValue.pkl')
    enc = OneHotEncoder()

    enc.fit_transform(train)
    data = enc.transform(train).toarray().astype(int)
    print('\n')
    print('--------------Training Classifier-----------',)
    clf = linear_model.SGDClassifier(loss='log',alpha=.01,verbose=2)
    clf.partial_fit(data,np.array(train_class),classes=np.array(uniqVal['class']))
    print('--------------------------------------------\n')
    # filename = 'DataChunks/chunk'+str(cntr)+'.pkl'
    # class_file = 'DataChunks/class'+str(cntr)+'.pkl'
    # joblib.dump(data, filename)
    # joblib.dump(train_class, class_file)
    return clf


if __name__ == '__main__':
    header = joblib.load('InputFiles/splits/header.pkl')
    with open('InputFiles/train.csv','r+') as f:
        rawdata0 = []
        header = []
        counter = 1
        cntr = 1
        uniqVal = joblib.load('DataChunks/uniqueValue.pkl')

        for line in f:
            if counter == 1:
                header = line.split(',')
                header = [x.strip('\n') for x in header if header != ""]
                joblib.dump(header,'InputFiles/splits/header.pkl')
                counter += 1
            else:
                rawdata0.append([x.strip('\n') for x in line.split(',') if x != ""])
                counter += 1

            if counter % 500000 == 0:
                # print('InputFiles/splits/D'+str(counter)+'.pkl')
                # fname = 'InputFiles/splits/D'+str(counter)+'.pkl'
                # joblib.dump(rawdata0, fname)
                classifier = trainClass(rawdata0, header, cntr, uniqVal)
                print('Counter :', counter)
                cntr += 1
                rawdata0 = []

        joblib.dump(uniqVal,'DataChunks/uniqueValue.pkl')
        joblib.dump(classifier,'classifier.pkl')
