import numpy as np
import matplotlib.pyplot as plt
from LightPipes import *

#*************** initial constants ***************#
wavelength=1000*nm
size=30*mm   # Size of the square grid
N=800           # The grid dimension
HoleSeparation=2*mm
z=300*cm      # Propagation distance
Nholes=6       # Number of Holes
size_hole=1*mm
HoleDiameter=0.5*mm

#*************** field in hole ***************#
Nhole=int(size_hole/size*N)
Fhole=Begin(size_hole,wavelength,Nhole)      # input field
Fhole1=CircAperture(Fhole,HoleDiameter/2)   # field to be inserted (Circle Aperture)

#*************** field in medium's grid ***************#
F0=Begin(size,wavelength,N)    # input field
F1=RowOfFields(F0,Fhole1,Nholes,HoleSeparation)  # separation of the inserted fields in the x-direction

#*************** propagation ***************#
F2=Lens(F1,z)   # Propagates the field through an ideal, thin lens (focus of the lens)
F3=Fresnel(F2,z)  # Propagate the field using a convolution method

#*************** intensity ***************#
I=Intensity(F3)  # Intensity in the screen

#*************** plot ***************#
plt.imshow(I,cmap='jet')
plt.axis('off')
plt.title('Intensity pattern (at the focus of the lens)')
plt.show()

