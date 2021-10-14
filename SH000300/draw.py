
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set(xlim=[0.5, 4.5], ylim=[-2, 8], title='An Example Axes',
       ylabel='Y-Axis', xlabel='X-Axis')

x = np.linspace(0, np.pi)
y_sin = np.sin(x)
y_cos = np.cos(x)

ax.plot(x, y_sin)
print(x)
print(y_sin)
plt.show()