from LightPipes import *
import matplotlib.pyplot as plt

# In a screen are illuminated by a plane wave
# With IntAttenuator we can split the field structure (amplitude division)
# The two obtained fields could be processed separately and then mixed again with the routine BeamMix
#************************************************************************************************************************

wavelength=5*um
size=20.0*mm  # Size of the square grid
N=500
z=50*cm         # The interference pattern at a distance z, behind the screen is calculated
R=0.2*mm      # Two holes with radious R
d=2*mm         # Two holes separated by d

#************************************************************************************************************************
# All the calculations must start with the Begin command. This command defines the size of the square grid, the grid dimension and the wave length of the field.
# Before any LightPipes commands the LightPipes package must be imported in your Python script.
# It is very convenient to use units. Units are included in the LightPipes package.

F=Begin(size,wavelength,N)
F1=CircAperture(F, R/2.0, -d/2.0, 0)
F2=CircAperture(F, R/2.0, d/2.0, 0)    
F=BeamMix(F1,F2)
F=Fresnel(z,F)  # Propagates the field using a convolution method , z (int, float) : propagation distance
I=Intensity(2,F)

#************************************************************************************************************************
# Plot
plt.imshow(I, cmap='jet')
plt.axis('off')
plt.title('intensity pattern')
plt.show()
