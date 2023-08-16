import matplotlib.pyplot as plt
import matplotlib.path as mpath
import numpy as np

verts = [
    (0, 0), # left, bottom
    (0, 1), # left, top
    (1, 1), # right, top
    (1, 0), # right, bottom
    (0, 0), # ignored
    ]

codes = [mpath.Path.MOVETO,
         mpath.Path.LINETO,
         mpath.Path.LINETO,
         mpath.Path.LINETO,
         mpath.Path.CLOSEPOLY,
         ]

icon = mpath.Path(verts, codes)

x=np.linspace(1,2,10)
y=np.sin(x)
plt.plot(x,y,marker=icon)

plt.show()
