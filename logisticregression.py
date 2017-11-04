# Logistic Regression using Stochastic Gradient Descent.
from math import exp

# make a prediction with coefficients using
# y = 1/(1 + e^(b0 + b1*x1))
def predict(row, coefficients):
    ypred = coefficients[0]
    for i in range(len(row)-1):
        ypred += coefficients[i+1] * row[i]
    return 1.0/(1.0 + exp(-ypred))

# estimate logistic regression coefficients using
# b = b + learning_rate * (y - ypred) * ypred * (1 - ypred) * x
def predict_coefficients(train, l_rate, n_epoch):
    # start with random initial values for coefficients.
    coef = [0.0 for i in range(len(train[0]))]
    for epoch in range(n_epoch):
        s_error = 0
        for row in train:
            ypred = predict(row, coef)
            error = row[-1] - ypred
            s_error += pow(error,2)
            coef[0] = coef[0] + l_rate * error * ypred * (1.0 - ypred)
            for i in range(len(row)-1):
                coef[i+1] = coef[i+1] + l_rate * error * ypred * (1.0 - ypred) * row[i]
        print ('epoch=%d,learning_rate=%.3f,error=%.3f' % (epoch, l_rate, s_error))
    return coef    

# training dataset.
dataset = [[2.7810836, 2.550537003, 0],
           [1.465489372, 2.362125076, 0],
	   [3.396561688, 4.400293529, 0],
	   [1.38807019, 1.850220317, 0],
	   [3.06407232, 3.005305973, 0],
	   [7.627531214, 2.759262235, 1],
	   [5.332441248, 2.088626775, 1],
	   [6.922596716, 1.77106367, 1],
	   [8.675418651, -0.242068655, 1],
	   [7.673756466, 3.508563011, 1]]

learning_rate = 0.3
num_epoch = 100
coef = coefficients_sgd(dataset, learning_rate, num_epoch)
print (coef)
    
    
