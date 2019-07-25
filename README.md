# Intelligent-Recycler
Código del proyecto ( Intelligent-Recycler )

Intelligent Recycler es un basurero inteligente clasificador de basura que funciona de manera autónoma utilizando inteligencia artificial. 

Su funcionamiento es el siguiente:  

En la parte superior se encuentra un sensor ultrasónico el cual detecta si se ha colocado un objeto. Luego se envía una señal al Raspberry pi para que la webcam tome una foto que luego es analizada por una AI(Inteligencia Artificial) creada con una Red Neuronal Convolucional, la cual tiene la capacidad de analizar y reconocer el tipo de basura que ha sido colocada, al ser reconocida se enciende el led que corresponde a su respectivo depósito, por la comunicación entre Raspberry pi y Arduino se envía una señal para que se active el motor paso a paso que hace girar el clasificador, cuando esto sucede el calificador se ubica en el depósito correspondiente y la tapadera se mueve para que basura sea depositada en su recipiente, por último la tapadera se vuelve a mover para que el basurero quede cerrado.



