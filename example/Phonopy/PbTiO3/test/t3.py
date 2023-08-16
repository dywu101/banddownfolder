import matplotlib.pyplot as plt
import matplotlib.path as mpath
import numpy as np

circle = mpath.Path.unit_circle()  # 获得一个圆 
verts_part= circle.wedge(340,220).vertices  # 按逆时针从340度到220度部分圆的路径点
codes_part = circle.wedge(340,220).codes  # 点类型 
verts_part = verts_part[1:-2]  # 去除第一个点和最后两个点 
codes_part = codes_part[1:-2] 
# 整合新的点 
verts = np.concatenate([np.array([[0,-2]]), verts_part, np.array([[0,-2]])]) 
codes = [mpath.Path.MOVETO] + codes_part.tolist() +  [mpath.Path.CLOSEPOLY] 

icon = mpath.Path(vertices=verts, codes=codes)

plt.plot(verts[:,0], verts[:,1]) 
plt.show() 

