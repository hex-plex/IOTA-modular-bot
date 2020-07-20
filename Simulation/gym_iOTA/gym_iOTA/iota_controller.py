import pybullet as p
import numpy as np
import cv2

iotas=[]
for i in range(n):
    iota=p.loadURDF('iota.urdf')
    iotas.append(iota)
