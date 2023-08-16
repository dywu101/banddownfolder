import numpy as np
import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatches


cc=mpath.Path.circle(center=(0,0),radius=0.1)
circle = mpath.Path.circle((0,0),1) 
icon = mpath.Path(verts, codes)

 
plt.plot(np.arange(5), np.arange(5), linestyle='', color='r', marker=icon, markersize=15)
plt.axis('equal')
plt.show()

