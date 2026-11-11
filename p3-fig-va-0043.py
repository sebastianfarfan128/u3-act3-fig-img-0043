import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

# Sebastian Farfan NC:0043 (10/11/26)
print("Sebastian Farfan")
print("UIII Act3 colocar puntos a una imagen en blanco y negro con VA")
Mi_imagen = cv2.imread('hola.jpg')
plt.imshow(Mi_imagen)
plt.title('hola (Sebastian Farfan NC:0043)')
plt.show()
print("--------+ Puntos en la imagen +--------")
plt.imshow(Mi_imagen)
x = [100,100,300,340]
y = [100,400,500,300]
plt.scatter(x, y, s=20,c='red')
plt.show()
print("+-+-+- Cuadro azul en la imagen +-+-+-+")
Mi_imagen = cv2.imread('hola.jpg')
plt.imshow(Mi_imagen)
# Nuevas coordenadas del cuadro
x = [200,200,600,600,200]
y = [600,200,200,600,600]
plt.plot(x,y, c='blue')
plt.show()
print("+-+-+- circulo verde en la imagen +-+-+-+")
I = cv2.imread('hola.jpg')
plt.imshow(I)
N = 30 # lados del poligono
x = np.zeros((N+1,))
y = np.zeros((N+1,))
(xc,yc) = (340,320)
r = 150 # radio
for i in range(N+1):
    t = 2*np.pi/N*i
    x[i] = xc + r*np.cos(t)
    y[i] = yc + r*np.sin(t)
plt.plot(x,y, c='green')
plt.show()