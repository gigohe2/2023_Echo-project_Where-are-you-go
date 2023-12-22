import numpy as np

import matplotlib.pyplot as plt
map = np.load('qr_map.npy')


print(np.shape(map))
print(map[0][0])
map[12,8] = 50
plt.imshow(map)
plt.show()