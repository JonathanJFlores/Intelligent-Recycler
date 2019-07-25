import sys
import os
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras import optimizers
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dropout, Flatten, Dense, Activation
from tensorflow.python.keras.layers import Convolution2D, MaxPooling2D
from tensorflow.python.keras import backend as K

K.clear_session() #matar sesiones abiertas

data_entrenamiento = './datapro/entrenamiento'
data_validacion = './datapro/validacion'

##------Parametros------

epocas = 20
altura, longitud = 100 , 100  #para redimensionar las imagenes
batch_size = 32 #numero de imagenes a enviar a procesar en cada paso
pasos = 500 #N de veces a procesar la informacion en cada epoca va tener 1000 pasos
pasos_validacion= 200 #al final de cada epoca se va a correr 200 pasos
filtrosConv1 = 32 #al final de la convolucion 1 la imagen va a tener una profundidad de 32
filtrosConv2 = 64  #al final de la convolucion  2 la imagen va a tener una profundidad de 64
tamano_filtro1 = (3,3) #filtro para la convolucion 1 altura, longitud
tamano_filtro2 = (2,2) #filtro para la convolucion 2
tamano_pool = (2,2) #tamaño del filtro para maxpooling
clases = 12 #etiquetas a reconocer(carpetas /plastico, papel, organicos, metal) 
lr = 0.0005 #que tan grandes son los ajustes que la RN hace para solucion optima

#----Pre procesamiento de Imagenes-----

entrenamiento_datagen = ImageDataGenerator(
    rescale = 1./255, # 0-255 px a 0-1 px para un entrenamiento mas optimo
    shear_range = 0.3,  #inclinar imagen
    zoom_range = 0.3, #para hacer zoom 
    horizontal_flip = True #invertir imagen(direccionamiento)
    )

validacion_datagen = ImageDataGenerator(
    rescale= 1./255 #imgenes como son, para validar 
    )

#--va entrar a las carpetas/imagenes le va adecuar altura y longitud y va ser de un modo categorico
imagen_entrenamiento = entrenamiento_datagen.flow_from_directory(
    data_entrenamiento,
    target_size = (altura , longitud),
    batch_size = batch_size,
    class_mode = 'categorical'
    )

imagen_validacion = validacion_datagen.flow_from_directory(
    data_validacion,
    target_size = (altura, longitud),
    batch_size = batch_size,
    class_mode = 'categorical'
    )

#--Red Neuronal Convolutional
cnn = Sequential() #varias capas apiladas 

#--1er capa de convolution y MaxPooling
cnn.add(Convolution2D(filtrosConv1, tamano_filtro1, padding='same', input_shape=(altura, longitud, 3), activation='relu'))
cnn.add(MaxPooling2D(pool_size = tamano_pool))

#--2er capa de convolution y MaxPooling
cnn.add(Convolution2D(filtrosConv2, tamano_filtro2, padding='same', activation='relu'))
cnn.add(MaxPooling2D(pool_size = tamano_pool))

#--Comienza la clasificación
cnn.add(Flatten()) #imagen un pequeña y profunda, va ser plana
cnn.add(Dense(256, activation='relu')) #imagen plana, capa con 256 neuronas que conecta a la capa anterior
cnn.add(Dropout(0.5)) #durante cada paso para que no se sobre ajuste, y pueda generalizar mejor a info nueva, evitar reajustar
cnn.add(Dense(clases, activation='softmax')) #para que de valores entre 0-1 capa de 3N- probabilidades en %

#--durante el entrenamiento la funcion de perdida es, optimizadose , metricas de de optimización(va mejorar que tan bien esta aprendiendo) 
cnn.compile(loss='categorical_crossentropy', optimizer = optimizers.Adam(lr=lr), metrics=['accuracy'])

#-Vamos entrenar RN imagenes  pre-procesadas, epocas 1000 pasos, en 1 epocas, correr 200 pasos de validación y luego se va a pasar a la siguiente epoca
cnn.fit_generator(
    imagen_entrenamiento, 
    steps_per_epoch=pasos,
    epochs=epocas, 
    validation_data=imagen_validacion, 
    validation_steps=pasos_validacion)

#--Guardar Modelo
dir = './modelo/'

if not os.path.exists(dir): #si no existe este directorio 
    os.mkdir(dir) #generarlo
cnn.save('./modelo/modelo1.h5') #guardar la estructura del modelo en el archivo
cnn.save_weights('./modelo/pesos1.h5') #guardar los pesos del modelo en el archivo
