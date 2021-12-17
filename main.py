import csv
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random

df = pd.read_csv("C:/Users/Administrator/Desktop/Python 2/classes/c111/studentMarks.csv")
data = df["Math_score"].tolist()


meanp = statistics.mean(data)

stdvp = statistics.stdev(data)
print("mean of population:",meanp)
print("stdv of population",stdvp)

def randommean(counter):
    dataset = []
    for i in range(0,counter):
        randomindex = random.randint(0,len(data)-1)
        value = data[randomindex]

        dataset.append(value)
    
    mean = statistics.mean(dataset)
    return mean

meanlist = []
for i in range(0,1000):
    setofmeans = randommean(100)
    meanlist.append(setofmeans)

#calculation mean and standard deviation of sampling

stdv = statistics.stdev(meanlist)
mean = statistics.mean(meanlist)

print("stdv of sampling", stdv)
print("mean of sampling",mean)


firststdvstart,firststend = mean-stdv , mean + stdv
secondstdvstart,secondstdvend = mean - (2*stdv), mean + (2* stdv)
thirdstdvstart, thirdstdvend = mean - (3*stdv),mean + (3*stdv)

print("stdv1:",firststdvstart,firststend )
print("stdv2:",secondstdvstart,secondstdvend)
print("stdv3:",thirdstdvstart,thirdstdvend)

fig = ff.create_distplot([meanlist],["mathscore"],show_hist=False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17],mode = "lines",name = "mean"))
fig.add_trace(go.Scatter(x = [firststdvstart,firststdvstart],y = [0,0.17],mode = "lines",name = "stdv1start"))
fig.add_trace(go.Scatter(x = [firststend,firststend],y = [0,0.17],mode = "lines",name = "stdv1end"))

fig.add_trace(go.Scatter(x = [secondstdvstart,secondstdvstart],y = [0,0.17],mode = "lines",name = "stdv2start"))

fig.add_trace(go.Scatter(x = [thirdstdvstart,thirdstdvstart],y = [0,0.17],mode = "lines",name = "stdv3start"))
fig.add_trace(go.Scatter(x = [thirdstdvend,thirdstdvend],y = [0,0.17],mode = "lines",name = "stdv2end"))




fig.show()

#this is for set of tablet students
df = pd.read_csv("C:/Users/Administrator/Desktop/Python 2/classes/c111/data1.csv")
data = df["Math_score"].tolist()

meanofsample1 = statistics.mean(data)
print("sample1 mean:",meanofsample1)

fig = ff.create_distplot([meanlist],["mathscore"],show_hist=False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17],mode = "lines",name = "mean"))
fig.add_trace(go.Scatter(x = [meanofsample1,meanofsample1],y = [0,0.17],mode = "lines",name = "mean of sample 1"))

fig.add_trace(go.Scatter(x = [firststend,firststend],y = [0,0.17],mode = "lines",name = "stdv1end"))
fig.show()


#this is the dataset of the extra class students
df = pd.read_csv("C:/Users/Administrator/Desktop/Python 2/classes/c111/data2.csv")
data = df["Math_score"].tolist()

meanofsample2 = statistics.mean(data)
print("sample2 mean:",meanofsample2)

fig = ff.create_distplot([meanlist],["mathscore"],show_hist=False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17],mode = "lines",name = "mean"))
fig.add_trace(go.Scatter(x = [meanofsample2,meanofsample2],y = [0,0.17],mode = "lines",name = "mean of sample 1"))

fig.add_trace(go.Scatter(x = [firststend,firststend],y = [0,0.17],mode = "lines",name = "stdv1end"))
fig.add_trace(go.Scatter(x = [secondstdvend,secondstdvend],y = [0,0.17],mode = "lines",name = "stdv2end"))

fig.show()

#dataset for fun sheet students

df = pd.read_csv("C:/Users/Administrator/Desktop/Python 2/classes/c111/data2.csv")
data = df["Math_score"].tolist()

meanofsample3 = statistics.mean(data)
print("sample3 mean:",meanofsample3)

fig = ff.create_distplot([meanlist],["mathscore"],show_hist=False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17],mode = "lines",name = "mean"))
fig.add_trace(go.Scatter(x = [meanofsample3,meanofsample3],y = [0,0.17],mode = "lines",name = "mean of sample 1"))

fig.add_trace(go.Scatter(x = [secondstdvend,secondstdvend],y = [0,0.17],mode = "lines",name = "stdv2end"))
fig.add_trace(go.Scatter(x = [thirdstdvend,thirdstdvend],y = [0,0.17],mode = "lines",name = "stdv2end"))

fig.show()

zscore1 = (mean - meanofsample1)/stdv
print("the zscore1 is:",zscore1)

zscore2 = (mean - meanofsample2)/stdv
print("the zscore2 is:",zscore2)

zscore3 = (mean - meanofsample3)/stdv
print("the zscore3 is:",zscore3)
