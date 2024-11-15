#super simmple use of matplot lib

import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 3, 3, 3.5, 4]

#plot these values
plt.scatter(x_values,y_values)
other_x = [1,2,3,4]
other_y = [2,4,6,8]
plt.plot(other_x,other_y)

plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Line and Scatter PLot")
plt.show()