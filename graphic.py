import matplotlib.pyplot as plt
from modules.graphic.gui import GUI


gui = GUI()
image = gui.capture()

plt.figure()
plt.imshow(image)
plt.show()
