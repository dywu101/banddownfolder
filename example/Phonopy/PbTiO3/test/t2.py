import matplotlib.pyplot as plt
import matplotlib.path as mpath
import numpy as np

star = mpath.Path.unit_regular_star(6)  # 星型Path
circle = mpath.Path.unit_circle()  # 圆形Path 

# 整合两个路径对象的点
verts = np.concatenate([circle.vertices, star.vertices[::-1, ...]])

# 整合两个路径对象点的类型
codes = np.concatenate([circle.codes, star.codes])

# 根据路径点和点的类型重新生成一个新的Path对象 
cut_star = mpath.Path(verts, codes)

#plt.plot(np.arange(10)**2, linestyle='', color='r', marker=cut_star, markersize=15)

#icon=mpath.Path.circle((0,0),1)
#icon=mpath.Path.arc(0,360,is_wedge=False)
#icon=mpath.Path.unit_circle().wedge(0,360)

icon=cut_star
plt.plot(np.arange(10)**2, linestyle='', color='r', marker=icon, markersize=15)

plt.show()

