# SNOW
Full Code for the [Beamline for Schools Challenge](https://beamlineforschools.cern/ )
Team SNOW - Spallation Neutron Optimisation, Tungsten

[Geant4](https://geant4.web.cern.ch/) was run via the [Gears](https://github.com/jintonic/gears) module, produced by [Dr Jing Liu](https://www.youtube.com/channel/UCQd4wp1ehUPXVHLjqYAMR3g) of the University of South Dakota. 
Many thanks to Dr Liu both for producing Gears, as well as for being willing to help us get started with Geant4.
  
## Contents:
- [Visualisation](https://github.com/33sah/SNOW/tree/main/Visualisation): Contains geometry of targets and world, as well as visualisation features - primarily used for debugging.
    ![Tungsten Cylinder 4GeV Protons](https://github.com/33sah/SNOW/assets/107648256/fbf3b6be-5da4-4976-8914-93c33383426a)[^1]
  
- [Movie](https://github.com/33sah/SNOW/tree/main/Movie): Contains code to make a Geant4 Movie, images collated to video using [FFmpeg](https://ffmpeg.org/).

  https://github.com/33sah/SNOW/assets/107648256/78297d9b-c158-4f38-aedf-bd2260a217b5
  
- [Data Production](https://github.com/33sah/SNOW/tree/main/Data%20Production): Python code to automate production of [ROOT](https://root.cern/) data files as well as raw Geant4 calculations.
  
- [Data Analysis](https://github.com/33sah/SNOW/tree/main/Data%20Analysis): Python - [Matplotlib](https://matplotlib.org/), [Seaborn](https://seaborn.pydata.org/) and [Uproot](https://uproot.readthedocs.io/) modules primarily used

Main Contributors: A.V, E.K[^2]

[^1]: Proton Path = Magenta, Neutron Path = Green
[^2]: Other Team Members Directly Referenced in Our Paper
