from ast import List, Param, main
from scipy.optimize import curve_fit
import uproot as up
import numpy as np
import itertools
import matplotlib
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
    for i in seq(2,31,1):
        Energy = str(round(i,1)).replace(".","_")
        path = f"A:/GEANT4/Target Geometry/Dimensions/{shape}/results{Energy}.root"
        file = up.open(path)
        t = file["t"]
        k = t.arrays(['k'], "pdg==2112") 
        final = ak.flatten(k, axis=None)
        mk = np.mean(final)
        dict[round(i,1)] = mk
    return dict
   
def canvas():
    global main 
    main = plt.figure(1,facecolor = "white")
    sea.set_style("ticks")
    plt.grid(linewidth = 0.1)
    sea.set_context("paper")
    sea.despine()
    plt.yticks(np.arange(0, 30000,2000 ))                                                                                                                                 
    
#generating blank dicts for each shape  
cyldict = {}

#collating data
collateData("cyl", cyldict)
print(max(list(cyldict.values())))

#plotting graphical info
canvas()
#find line of best fit
a, b = np.polynomial.polynomial.polyfit(list(cyldict.keys()), list(cyldict.values()), 1)
#add points to plot
plt.scatter(list(cyldict.keys()),cyldict.values())
#add line of best fit to plot
plt.plot(list(cyldict.keys()), b*np.array(list(cyldict.keys())) + a)

plt.legend(loc = "upper left", prop={'size': 5})
plt.title("Neutron Energy vs Cylinder Height")
plt.xlabel("Height of Cylinder (cm)")
plt.ylabel("Mean Kinetic Energy of Neutrons (KeV)")
import tikzplotlib as tk
tk.save("CylinderEnergy.tex")
plt.show()




