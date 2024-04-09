import uproot as up
import matplotlib.pyplot as plt
import awkward as ak
import seaborn as sea
import tikzplotlib as tk

file = up.open("D:/Asa/geant4-11.2.1/gears-master/Sub Critical Spallation/Pythontry/Shapes/cyl/results3_0cyl.root")
t = file["t"]

k = t.arrays(['k'],"pro==1000")
array = ak.flatten(k, axis=None)
data = {"emergy":array}

# Plot the histogram.
sea.histplot(data=data, x="emergy", kde=True,palette="light:m_r", edgecolor=".3", linewidth=.5,color = "blue")
sea.set_style("ticks")
plt.grid(linewidth = 0.1)
sea.set_context("paper")

 
# Plot the PDF.
title = "Gaussian Profile of Proton Energy"
plt.xlabel("Energy of Protons (keV)")
plt.ylabel("Number of Protons")
plt.legend(["Kernel Density Estimate","Histogram"])
plt.title(title)
plt.rcParams['figure.dpi'] = 360
tk.save("Energy_Distribution.tex")
 
plt.show()