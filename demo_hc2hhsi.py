# This demo shows how to transform a four-dimensional hypercube to the hhsi space.
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from hc2hhsi import hc2hhsi

# Read RGB-colour and near-infrared images
VIS = mpimg.imread('VIS.png')
NIR = mpimg.imread('NIR.png')
NIR = NIR[1:965, :] # The NIR image should have the same size as the VIS image.

plt.figure(1)
plt.subplot(121)
plt.imshow(VIS)
plt.title('RGB colour image')
plt.subplot(122)
plt.imshow(NIR, cmap='gray')
plt.title('Near infrared image')

# Stack the NIR and VIS images to a four-dimensional hypercube.
hc = np.dstack((NIR, VIS))

# Transform the hypercube to the hhsi space.
hh, s, i = hc2hhsi(hc)

plt.figure(2)
plt.subplot(231)
plt.imshow(hh[:, :, 0], cmap='gray')
plt.title('Hyper hue 1')
plt.subplot(232)
plt.imshow(hh[:, :, 1], cmap='gray')
plt.title('Hyper hue 2')
plt.subplot(233)
plt.imshow(hh[:, :, 2], cmap='gray')
plt.title('Hyper hue 3')
plt.subplot(234)
plt.imshow(s, cmap='gray')
plt.title('Saturation')
plt.subplot(235)
plt.imshow(i, cmap='gray')
plt.title('Intensity')
plt.show()

