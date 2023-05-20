import numpy as np
#Learning matplotlib
#pyplot is a module within the matplotlib library, which is a
#popular plotting library in Python. pyplot provides a simple interface for creating
#various types of plots, such as line plots, scatter plots, bar plots, histograms, and more.

import matplotlib.pyplot as plt

#creates a line splot
x1 = [1,2,3,4]
y1 = [1,2,3,4]
plt.plot(x1,y1,marker ='*',color='orange',label='aline')

#These are used to indicate the x, y  lable and title of the plot.
plt.title('Demo')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.show()


#Used numpy to define x and y random datas
data = np.random.rand(2,10)
sdata = np.split(data,2,axis=0)
x = sdata[0]
y = sdata[1]

#Creates a scatter plot for the above x and y
plt.scatter(x,y,marker='o',color='red')
plt.legend(['data'])
plt.show()

