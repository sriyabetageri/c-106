import plotly.express as px
import csv
import numpy as np

def getDataSource(dataPath):
    sTV=[]
    aT = []
    with open(dataPath) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            sTV.append(float(row["Size of TV"]))
            aT.append(float(row["\tAverage time spent watching TV in a week (hours)"]))
    return{"x":sTV, "y": aT}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("correlation between Size of TV and Average time spent watching TV in a week (hours): \n",correlation[0,1])

def setUp():
    dataPath = "STAT.csv"
    dataSource = getDataSource(dataPath) 
    findCorrelation(dataSource)

setUp()  