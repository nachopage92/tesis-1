import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

points = [(3.28,0.00),(4.00,0.50),(4.40,1.0),(4.60,1.52),(5.00,2.5),(5.00,3.34),(4.70,3.8)]
points = points + [(4.50,3.96),(4.20,4.0),(3.70,3.90),(3.00,3.5),(2.00,2.9)]
points = points + [(3.28,0.00)]
data = np.array(points)

print(points)

knots = np.arange(0.0,1.0,1.0/(len(points)))
print(knots)

input()

#tck,u = interpolate.splprep(data.transpose(), s=2)
tck,u = interpolate.BSpline(knots,data.transpose(),2)
unew = np.arange(0, 1.01, 0.01)
out = interpolate.splev(unew, tck)

print(out)

plt.figure()
plt.axis('off')
plt.plot(out[0], out[1], color='orange')
plt.plot(data[:,0], data[:,1], 'ob')
plt.show()
