# Resampling Techniques/k-fold Cross Validation

# divide the dataset into training and test set.
def dividedata(data, test=0.10):
    trainset = []
    testset = []
    for row in data:
        if random() < test:
            testset.append(row)
        else:
            trainset.append(row)
    return (trainset,testset)

# calculate root mean squared error.
def testalgorithm(algf,trainset,testset):
    rmse = 0.0
    for row in testset:
        guess = algf(trainset, row['input'])
        rmse += pow((row['result']-guess),2)
    return rmse/len(testset)

# cross validation with 10 trials.
def crossvalidate(algf,data,trials=10,test=0.10):
    error = 0.0
    for i in range(trials):
        (trainset,testset) = dividedata(data,test)
        error += testalgorithm(algf,trainset,testset)
    return error/trials
