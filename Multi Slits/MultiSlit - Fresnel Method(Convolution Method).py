import numpy as np
import matplotlib.pyplot as plt
from LightPipes import *

#*************** initial constants ***************#
wavelength=1000*nm
size=11*mm   # Size of the square grid
N=2000   # The grid dimension
SlitSeparation=0.5*mm
z=30*cm   # Propagation distance
Nslits=20  # Number of Slits
SlitHeight=5*mm
SlitWidth=0.1*mm

#*************** field in hole ***************#
Nheight=int(SlitHeight/size*N)
Nwidth=int(SlitWidth/size*N)

Fslit=np.ones((Nheight,Nwidth))  # Creating Multi-dimensional array
#print(Fslit)
F1=Begin(size,wavelength,N)    # input field
F2=RowOfFields(F1,Fslit,Nslits,SlitSeparation)  # separation of the inserted fields in the x-direction

#*************** propagation ***************#
F3=Lens(F2,z)   # Propagates the field through an ideal, thin lens (focus of the lens)
F4=Fresnel(F3,z)  # Propagate the field using a convolution method

#*************** intensity ***************#
Iscreen=Intensity(F4)

#*************** plot ***************#
plt.imshow(Iscreen,cmap='jet')
#plt.axis('off')
plt.title('Intensity pattern (at the focus of the lens)')
plt.show()

