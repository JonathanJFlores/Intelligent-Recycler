# Intelligent-Recycler
Código del proyecto ( Intelligent-Recycler )

Intelligent Recycler es un basurero inteligente clasificador de basura que funciona de manera autónoma utilizando inteligencia artificial. 

Su funcionamiento es el siguiente:  
En la parte superior se encuentra un sensor ultrasónico el cual detecta si se ha colocado un objeto. Cuando una persona deposita basura el sensor detecta que hay un objeto frente a el, luego se envía una señal para que la webcam tome una foto que es analizada por una AI creada con una Red Neuronal Convolucional que la cual tiene la capacidad de clasificar el tipo de basura que ha sido colocada, al ser clasificada se activa el led que corresponde a su respectivo deposito, esto por medio de la microPC (Raspberry Pi 3 B+), luego se activa el motor paso a paso que hace funcionar el clasificador, por medio de la placa controladora Arduino, cuando esto sucede el calificador se ubica en el depósito correspondiente y la basura es depositada en su recipiente.

