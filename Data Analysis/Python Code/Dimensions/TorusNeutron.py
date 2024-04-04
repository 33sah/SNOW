from ast import List, Param, main
from scipy.optimize import curve_fit
import uproot as up
import numpy as np
import itertools
import matplotlib.pyplot as plt
import seaborn as sea
import awkward as ak
import pandas as pd

#indexing
def seq(start, end, step):
    if step == 0:
        raise ValueError("step must not be 0")
    sample_count = int(abs(end - start) / step)
    return itertools.islice(itertools.count(start, step), sample_count)


#function takes a dictionary and returns it with EK values for input shape.
#shape must be "box", "cone", "cyl", "hype", "sph", "tor"  
#VERY SYSTEM DEPENDANT, adjust code to fit ur paths or adjust paths to fit code
def collateData(shape, dict,):
    dict.clear()
    for i in seq(1.00,1.73,0.02):
        Energy = str(round(i,2)).replace(".","_")
        path = f"A:/GEANT4/Target Geometry/Dimensions/{shape}/results{Energy}.root"
        file = up.open(path)
        t = file["t"]
        n = t.arrays(['pdg'], "pdg==2112")
        final2 = len(ak.flatten(n, axis=None))/1000
        dict[round(i,2)] = final2
    return dict

def canvas():
    global main 
    main = plt.figure(1,facecolor = "white")
    sea.set_style("ticks")
    plt.grid(linewidth = 0.1)
    sea.set_context("paper")
    sea.despine()
    plt.yticks(np.arange(0, 120,10 ))                                                                                                                                 

#generating blank dicts for each shape  
tordict = {}

#collating data
collateData("tor", tordict)

print(len(tordict.keys()))
print(len(tordict.values()))
#plotting graphical info
canvas()
#find line of best fit
a, b = np.polynomial.polynomial.polyfit(list(tordict.keys()), list(tordict.values()), 1)
#add points to plot
plt.scatter(list(tordict.keys()), tordict.values())
#add line of best fit to plot
plt.plot(list(tordict.keys()), b*np.array(list(tordict.keys())) + a)

plt.legend(loc = "upper left", prop={'size': 5})
plt.title("Neutrons per proton vs Inner Radius of Torus")
plt.xlabel("Inner Radius of Torus (cm)")
plt.ylabel("Neutrons Produced per Incident Proton")
import tikzplotlib as tk
tk.save("TorusNeutron.tex")
plt.show()




