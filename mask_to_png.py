from matplotlib import gridspec
from matplotlib import pyplot as plt
from matplotlib import image
import numpy as np


masks = np.load("masks.npy")
plt.imshow(masks[0])
plt.imsave('s-mask.png', masks[0], cmap=plt.get_cmap("gray"))
