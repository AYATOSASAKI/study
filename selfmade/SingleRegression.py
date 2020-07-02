import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

d = np.array([[0.162776,23.708768],[0.881034,22.974510]])
dataset = pd.DataFrame(data=d)

x1 = d[0][0]
y1 = d[0][1]

x2 = d[1][0]
y2 = d[1][1]

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(x1,y1)
ax.scatter(x2,y2)

ax.set_title('relation between output current and load voltage')
ax.set_xlabel('output current [A]')
ax.set_ylabel('load voltage [V]')
plt.show()