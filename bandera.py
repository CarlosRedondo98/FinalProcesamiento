# imports
import numpy as np
import cv2
import os

class bandera:

    # Constructor
    def __init__(self, rutaImagen):
        self.imagen = cv2.imread(rutaImagen, 1)  # imagen importada

    # Métodos
    def colores (self):
        image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)

        n_colors = 4
        image = np.array(image, dtype=np.float64) / 255
        rows, cols, ch = image.shape
        assert ch == 3
        image_array = np.reshape(image, (rows * cols, ch))
        image_array_sample = shuffle(image_array, random_state=0)[:10000]
        model = KMeans(n_clusters=n_colors, random_state=0).fit(image_array_sample)
        labels = model.predict(image_array)
        centers = model.cluster_centers_
        Num_colors = np.max(labels) + 1
        print('Numero de colores', Num_colors)


