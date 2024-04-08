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
        path = f"A:/GEANT4/Analysis/10k protons/results{Energy}{shape}.root"
        file = up.open(path)
        t = file["t"]
        k = t.arrays(['k'], "pdg==2112")
        final = ak.flatten(k, axis=None)
        mk = np.mean(final)
        dict[round(i,1)] = mk
    return dict
    
#Logarithmic Function Template
def log_f(x,a,b):
    return a+ b*np.log(x) 

#takes x data and y data as input, fits to a LOG function
def fitLog(x, y):
    param, param_cov = curve_fit(log_f,x,y)
    print("Log Coefficients")
    print(param) #a and b parameters can be read from here.
    answer = log_f(x, param[0], param[1])
    return answer

#generally sets up canvas, takes y data to scale axis
def canvas(y):
    global main 
    main = plt.figure(1,facecolor = "white")
    sea.set_style("ticks")
    plt.grid(linewidth = 0.1)
    sea.set_context("paper")
    sea.despine()
    plt.yticks(np.arange(0, max(y), 2500))                                                                                                                                 
    
#takes x values, y values shape name and desired colour. 
#plots raw data along with log fitted curve    
def quickPlot(x,y,shape, colour ):
    plt.plot(x, y, 'o', color = colour, label = shape)
    plt.plot(x, fitLog(x,y), '--', color = colour, label ="Fitted Data for " + shape)

#generating blank dicts for each shape  
tordict = {}

#collating data

collateData("tor", tordict)

print(max(tordict.values()))
#plotting graphical info
canvas(list(tordict.values()))

quickPlot(list(tordict.keys()), list(tordict.values()), "Torus", "black")
plt.legend(loc = "upper left", prop={'size': 10})
plt.title("Neutron Energy vs Proton Energy (10K Protons)")
plt.xlabel("Energy of Protons (GeV)")
plt.ylabel("Mean Kinetic Energy (keV)")
import tikzplotlib as tk
tk.save("TorusEnergy10k.tex")
plt.savefig("TorusEnergy10k.png", dpi = 1000)
plt.show()



