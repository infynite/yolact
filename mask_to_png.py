from matplotlib import gridspec
from matplotlib import pyplot as plt
from matplotlib import image
import numpy as np

def mask_save(np_mask, path):
  plt.imsave(path, np_mask[0], cmap=plt.get_cmap("gray"))
