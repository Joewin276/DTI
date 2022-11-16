import sys
import matplotlib

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([2, 4, 6, 10])

plt.plot(ypoints, 'o:r')
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()