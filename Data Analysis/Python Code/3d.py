import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sea
import numpy as np
import uproot as up
import awkward as ak

sea.set_theme(style = "white", context = "notebook")
file = up.open("D:/Asa/geant4-11.2.1/gears-master/Sub Critical Spallation/Pythontry/Shapes/cyl/results3_0cyl.root")
t = file["t"]

x = t.arrays(['x'],"k>1000000")
x_new = ak.flatten(x, axis=None)

y = t.arrays(['y'],"k>1000000")
y_new = ak.flatten(y, axis=None)

z= t.arrays(['z'],"k>1000000")
z_new = ak.flatten(z, axis=None)


plt.figure (figsize = (6,6))
seaborn_plot = plt.axes (projection='3d')
print (type (seaborn_plot))
seaborn_plot.scatter3D (x_new, y_new, z_new, color = "#FF3131")
seaborn_plot.set_xlabel ('Distance from X axis (mm)')
seaborn_plot.set_ylabel ('Distance from Y axis (mm)')
seaborn_plot.set_zlabel ('Distance from Z axis (mm)')
seaborn_plot.set_title("Distribution of Collisions")
plt.show ()