from LightPipes import *
import matplotlib.pyplot as plt

# In a screen are illuminated by a plane wave

#************************************************************************************************************************

wavelength=5*um
size=30.0*mm  # Size of the square grid
N=1000
z=30*cm         # The interference pattern at a distance z, behind the screen is calculated

#************************************************************************************************************************
# All the calculations must start with the Begin command. This command defines the size of the square grid, the grid dimension and the wave length of the field.
# Before any LightPipes commands the LightPipes package must be imported in your Python script.
# It is very convenient to use units. Units are included in the LightPipes package.

F0=Begin(size,wavelength,N)
F1 = PointSource(F0, 0.0, 0.0)
F2 = Fresnel(z,F1)  # Propagates the field using a convolution method , z (int, float) : propagation distance (Forward)
I = Intensity(2,F2)  # 2 means ==> matrix 2*2

#************************************************************************************************************************
# Plot
plt.imshow(I, cmap='jet')
plt.axis('off')
plt.title('intensity pattern')
plt.show()
