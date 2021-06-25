import math
import csv

with open('data.csv',newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)

data=file_data[0]
def getMean(data):
    n=len(data)
    total=0
    for i in data:
        total+=int(i)
    mean=total/n
    return mean

sq_list=[]
for j in data:
    sub=int(j)-getMean(data)
    sub=sub**2
    sq_list.append(sub)

s=0
for h in sq_list:
    s=s+h
res=s/(len(data)-1)
sd=math.sqrt(res)
print(sd)
    