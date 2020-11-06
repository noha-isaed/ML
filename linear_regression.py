import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# read the data
data = pd.read_excel(r'data.xls')
data

# get a feeling about the data
data.head()

# take values of X alon and values of Y alon
X_train = data['X']
Y_train = data['Y']

# plot the relationship between X & Y
plt.scatter(X_train, Y_train, alpha=1)
plt.title('Scatter plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

# try to find values of Theata0 & Theta1 by using the linear regression equation
Theta0 = 0
Theta1 = 0
Alpha = 0.0003
Y_Predict = 0


for i in range(10000):
    
    Y_Predict = Theta0 + ( Theta1 * X_train ) 
        
    Theta0 = Theta0 - Alpha*(1/len(data))*sum(Y_Predict - Y_train)
        
    Theta1 = Theta1 - Alpha*(1/len(data))*sum(X_train * (Y_Predict - Y_train))


#open txt file and add values of theta0 & theta1 to this file
parameters_file = open("parameters.txt","w+") 
parameters_file.write("Theta0 = " + str(Theta0) +"\n")

parameters_file.write("Theta1 = "  + str(Theta1))
parameters_file.close()


# find value of y_predict for each X and store it in list then add this list as column in data
Y_Predict  =[] 
y_predict = 0
for j in range(len(data)):
        y_predict = Theta0 + (Theta1*X_train[j]) 
        Y_Predict.append(y_predict)
        y_predict = 0
data['Y_Predict'] = Y_Predict

print(data)


# plot the relationship between y_predict & X to sure if values of theta0 & theta1 is true or false 
plt.scatter(X_train,Y_train , color='black' , alpha=1)
plt.plot(X_train, Y_Predict, color='blue', linewidth=2)

plt.xlabel('X')
plt.ylabel('Y')


plt.show()