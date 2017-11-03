# Simple Linear Regression.
from math import sqrt

# mean value of list of numbers.
def mean(values):
    return sum(values)/float(len(values))

# variance is the sum squared difference for each value
# from the mean value.
def variance(values, mean):
    return sum([(x - mean)**2 for x in values])

# covariance of two groups of numbers describes
# how those numbers change together.
def covariance(x, mean_x, y, mean_y):
    covar = 0.0
    for i in range(len(x)):
        covar += (x[i] - mean_x) * (y[i] - mean_y)
    return covar

# calculate coefficients
def coefficients(dataset):
    x = [row[0] for row in dataset]
    y = [row[1] for row in dataset]
    (x_mean, y_mean) = (mean(x), mean(y))
    b1 = covariance(x, x_mean, y, y_mean)/variance(x, x_mean)
    b0 = y_mean - b1 * x_mean
    return (b0, b1)

# simple linear regression.
def simple_linear_regression(train, test):
    predictions = list()
    (b0,b1) = coefficients(train)
    for row in test:
        ypred = b0 + b1 * row[0]
        predictions.append(ypred)
    return predictions

# calculate root mean squared error.
def root_mean_squared_error(actual, predicted):
    sum_error = 0.0
    for i in range(len(actual)):
        prediction_error = predicted[i] - actual[i]
        sum_error += (prediction_error ** 2)
    mean_error = sum_error/float(len(actual))
    return sqrt(mean_error)
