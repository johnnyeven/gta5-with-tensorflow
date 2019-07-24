import platform
import cv2
import numpy as np

from modules.graphic.gui_mac import _MacAdapter
from modules.graphic.gui_window import _WindowAdapter


class GUI:
    __adapter = None
    __platform = ""

    def __init__(self):
        self.__platform = platform.system()
        if self.__platform == "Windows":
            self.__adapter = _WindowAdapter()
        elif self.__platform == "Linux":
            pass
        else:
            self.__adapter = _MacAdapter()
        print(self.__platform)

    def capture(self):
        data, width, height = self.__adapter.capture()
        image = np.fromstring(data, dtype='uint8')
        image.shape = (height, width, 4)
        return cv2.cvtColor(image, cv2.COLOR_BGRA2RGB)
