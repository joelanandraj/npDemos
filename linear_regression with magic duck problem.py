import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression #sklearn is a library, linear_model is a module
# Linear Regression is a Class, Here we are importing only one class.
from sklearn.model_selection import train_test_split

from sklearn.metrics import mean_squared_error,r2_score

data = pd.read_csv('MAGICDUCK.csv')  #loaded the data from magicduck file and stored in data.

#print(data.describe())

x = data['Day']
print(x)
x = x.values.reshape(-1,1) #We reshape 'x' using the .values.reshape(-1, 1) method to
#ensure it has the shape(n_samples, n_features) required by scikit-learn

y = data['Egg']


#plt.plot(x,y,marker='*',color="blue",label='EggCount')
#plt.legend()
#plt.show()

model = LinearRegression()
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state = 42)
#By setting a specific value for random_state, you can ensure that the train-test split
#is reproducible. Providing the same random_state value will result in the same train-test split
#every time you run your code.

model.fit(xtrain,ytrain)

ypredict = model.predict(xtest)

plt.plot(xtest,ytest,marker='o',color='red',label='observed')
plt.plot(xtest,ypredict,marker='*',color='white',label="prediction")
plt.legend()
plt.show()

mse = mean_squared_error(ytest,ypredict)
r2 =r2_score(ytest,ypredict)
print("Mean Squared Error : {0}".format(mse))
print("R2 Score  {0}".format(r2))
