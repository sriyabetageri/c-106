import plotly.express as px
import csv
import numpy as np

def getDataSource(dataPath):
    isales=[]
    csales = []
    with open(dataPath) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            isales.append(float(row["Temperature"]))
            csales.append(float(row["Ice-cream Sales( ₹ )"]))
    return{"x":isales, "y": csales}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("correlation between ice cream and temerature: \n",correlation[0,1])

def setUp():
    dataPath = "ICT.csv"
    dataSource = getDataSource(dataPath) 
    findCorrelation(dataSource)

setUp()  