import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
import h5py

longitud, altura = 100, 100
modelo='./modelo/modelo1.h5'
pesos='./modelo/pesos1.h5'

cnn=load_model(modelo) #cargar el modelo en cnn
cnn.load_weights(pesos) #cargar al modelo los pesos 
 
def predict(file):
    x= load_img(file, target_size=(longitud, altura)) #cargar la imagen a x con la longitud y altura definida anteriormente 
    x= img_to_array(x) #-imagen ahora es un arreglo
    x= np.expand_dims(x, axis=0) #en eje 0 añadir una dimension mas, para poder procesar mejor la información 
    array= cnn.predict(x) ##-queremos hacer una prediccion y traer un arreglo de dos dimensiones [[1,0,0]] 
    resultado= array[0] #traer la primera dimension ##[1,0,0]
    respuesta= np.argmax(resultado) #-para traer el valor mas alto en el arreglo #[0]
    return respuesta # regresamos el número con mayor porcentaje el que este más cerca al 1  
