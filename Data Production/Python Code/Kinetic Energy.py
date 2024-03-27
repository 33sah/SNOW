from ast import List, Param
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
#shape must be "Torus", "Sphere" or "Cylinder"  
#VERY SYSTEM DEPENDANT, adjust code to fit ur paths or adjust paths to fit code
def collateData(shape, dict):
    dict.clear()
    for i in seq(0.1,5,0.1):
        Energy = str(round(i,1)).replace(".","_")
        match shape:
            case "Sphere":
                path = f"A:/GEANT4/1000 Protons/{shape}/results{Energy}sph.root" #beginning of paths need ajustment to work on ur system!
            case "Torus":
                path = f"A:/GEANT4/1000 Protons/{shape}/results{Energy}TOR.root"
            case "Cylinder":
                path = f"A:/GEANT4/1000 Protons/{shape}/results{Energy}pleasework.root"
            case _:
                raise TypeError("You probably put the wrong shape formatting in. Blame Eesah.") 
        file = up.open(path)
        t = file["t"]
        k = t.arrays(['k'], "pdg==2112") # get all x in vlm 1
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
    print(param)
    answer = log_f(x, param[0], param[1])
    return answer

#generally sets up canvas, takes y data to scale axis
def canvas(y):
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
sphDict = {}
torDict = {}
cylDict = {}
#collating data
collateData("Sphere", sphDict)
collateData("Torus", torDict)
collateData("Cylinder",cylDict)
canvas(list(torDict.values()))
#plotting graphical info
quickPlot(list(sphDict.keys()), list(sphDict.values()), "Sphere", "#06F50D")
quickPlot(list(torDict.keys()), list(torDict.values()), "Torus", "#34cfeb")
quickPlot(list(cylDict.keys()), list(cylDict.values()), "Cylinder", "#F50E16")
plt.legend()
plt.title("Average Kinetic Energy of Neutrons vs Proton Energy - 1000 Protons")
plt.xlabel("Energy of Protons (GeV)")
plt.ylabel("Average Kinetic Energy (KeV)")
plt.show()

