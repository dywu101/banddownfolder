import matplotlib.pyplot as plt
import matplotlib.path as mpath
import numpy as np

circle = mpath.Path.unit_circle()  # 获得一个圆 
verts_part = circle.wedge(0,360).vertices
codes_part = circle.wedge(0,360).codes
#print(verts_part)
#print(codes_part)
verts_part = verts_part[1:-2]  # 去除第一个点和最后两个点 
codes_part = codes_part[1:-2] 


# center of circle
cc = mpath.Path.circle(center=(0,0),radius=0.1)
cc_verts=cc.vertices
cc_codes=cc.codes



# 整合新的点 
verts = np.concatenate([np.array([[1,0]]), verts_part, np.array([[1,0]])]) 
codes = [mpath.Path.MOVETO] + codes_part.tolist() +  [mpath.Path.CLOSEPOLY] 

#verts=cc_verts
#codes=cc_codes

#print(verts)
#print(codes)
#verts=verts_part
#codes=codes_part

icon = mpath.Path(vertices=verts, codes=codes)


#plt.plot(verts[:,0], verts[:,1]) 
#plt.axis('equal')
#plt.show() 


plt.scatter(np.arange(1,5),np.arange(1,5), marker=icon, s=300, facecolor="none",edgecolors="black")
plt.axis('equal')
plt.show()

