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
    for i in seq(0.5,5.1,0.1):
        Energy = str(round(i,1)).replace(".","_")
        path = f"A:/GEANT4/Analysis/1000 protons/results{Energy}{shape}.root"
        file = up.open(path)
        t = file["t"]
        k = t.arrays(["de"], "pdg==2212")
        final = ak.flatten(k, axis=None)
        mk = np.mean(final)
        dict[round(i,1)] = mk
    return dict
    
#Reciprocal Function Template
def rec(x,a,b):
    return a/x + b 

#takes x data and y data as input, fits to a reciprocal function
def fit(x, y):
    param, param_cov = curve_fit(rec,x,y)
    print("Coefficients")
    print(param) #a and b parameters can be read from here.
    answer = rec(x, param[0], param[1])
    return answer

#generally sets up canvas, takes y data to scale axis
def canvas(y):
    global main 
    main = plt.figure(1,facecolor = "white")
    sea.set_style("ticks")
    plt.grid(linewidth = 0.1)
    sea.set_context("paper")
    sea.despine()
    plt.yticks(np.arange(0, 16000, 1000))                                                                                                                                 
    
#takes x values, y values shape name and desired colour. 
#plots raw data along with reciprocalfitted curve    
def quickPlot(x,y,shape, colour ):
    plt.plot(x, y, 'o', color = colour, label = shape)
    plt.plot(x, fit(x,y), '--', color = colour, label ="Fitted Data for " + shape)

#generating blank dicts for each shape  
tordict = {}
sphdict = {}
cyldict = {}

#collating data

collateData("tor", tordict)
collateData("cyl", cyldict)
collateData("sph", sphdict)
print(max(cyldict.values()))
#plotting graphical info
canvas(list(tordict.values()))

quickPlot(list(tordict.keys()), list(tordict.values()), "Torus", "black")
quickPlot(list(cyldict.keys()), list(cyldict.values()), "Cylinder", "red")
quickPlot(list(sphdict.keys()), list(sphdict.values()), "Sphere", "green")

plt.legend(loc = "upper left", prop={'size': 5})
plt.title("Energy Deposited in Target (per proton) vs Proton Energy")
plt.xlabel("Proton Energy GeV")
plt.ylabel("Energy Depositied Per Incident Proton (keV)")
import tikzplotlib as tk
tk.save("Deposition.tex")
plt.savefig("Deposition.png", dpi = 1000)
plt.show()



