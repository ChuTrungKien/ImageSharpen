import cv2
import numpy as np
from matplotlib import pyplot as plt

#Doc anh dau vao:
imgInput = cv2.imread("File_anh_dau_vao")

#Chuyen doi hinh anh tu BGR -> RGB:
imgRGB = cv2.cvtColor(imgInput, cv2.COLOR_BGR2RGB)

