# K-Nearest Neighbor.
import math

# parse data from file [input=(5.9,3.0,5.1,1.8),result='Iris-virginica']
file = open('dataset.txt', 'r')
lines = [line for line in file]
dataset = []
for line in lines:
    data = line.strip().split(',')
    dataset.append({'input':(float(data[0]),float(data[1]),float(data[2]),float(data[3])),
                    'result':data[4]})

# similarity score for two records.
def euclidean(v1,v2):
    distance = 0.0
    for i in range(len(v1)):
        distance += pow((v1[i]-v2[i]),2)
    return math.sqrt(distance)

# get 'k' nearest neighbors.
def getneighbors(v1, k=3):
    neighbors = []
    for i in range(len(dataset)):
        v2 = dataset[i]['input']
        neighbors.append((euclidean(v1,v2), i))
    neighbors.sort()
    return neighbors[0:k]

# predict the response.
def getresponse(neighbors):
    classvotes = {}
    for i in range(len(neighbors)):
        prediction = dataset[neighbors[i][1]]['result']
        classvotes.setdefault(prediction, 1)
        classvotes[prediction] += 1
    sortedvotes = sorted(classvotes, key=classvotes.get, reverse=True)
    return sortedvotes[0]

neighbors = getneighbors((5.9,3.0,5.1,1.8))
print (getresponse(neighbors))
        
    
