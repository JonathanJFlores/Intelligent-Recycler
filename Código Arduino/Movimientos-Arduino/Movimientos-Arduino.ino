#include <Stepper.h>
#include <Servo.h>

int Trig = 5; //pin para disparo ultrasonido
int Echo = 6; //pin para recepcion del ultrasonido

long duracion; //variable para guardar el tiempo en recibir el disparo 
float distancia; //variable para operar la distancia 

// Declaramos la variable para controlar el servo
Servo servoMotor;

//Servo Dispensador
Servo myservo;  // crea el objeto servo
int vel = 0;    // velocidad del servo
 

//definimos los pines y parametros del motor paso a paso 
Stepper motor1(2048, 8, 10, 9, 11);

int ledverde = A0;
int ledblanco = A1;
int ledazul = A2;
int lednaranja = A3;
int ledrojo = A4;

void setup() {
  Serial.begin(9600);
  delay(1000);

  pinMode(Trig, OUTPUT);
  pinMode(Echo, INPUT);

  motor1.setSpeed(2); //en RPM( valores de 1,2,3)

  pinMode(ledverde, OUTPUT);
  pinMode(ledblanco, OUTPUT);
  pinMode(ledazul, OUTPUT);
  pinMode(lednaranja, OUTPUT);
  pinMode(ledrojo, OUTPUT);

  //Servo tapa
  servoMotor.attach(7);
}

void loop() {
  //iniciar los leds en estado apagado (LOW)
  digitalWrite(ledverde, LOW);
  digitalWrite(ledblanco, LOW);
  digitalWrite(ledazul, LOW);
  digitalWrite(lednaranja, LOW);
  digitalWrite(ledrojo, LOW);

  //Sensor ultrasonido
  digitalWrite(Trig, LOW);
  delayMicroseconds(2);
  digitalWrite(Trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(Trig, LOW);

  //calcular la distancia 
  duracion = pulseIn(Echo, HIGH);
  distancia = (duracion/2)/29.15;

  delay(50);
  
  if (distancia >0 && distancia < 15){
    Serial.println("foto"); //envía la palabra foto a Raspberry pi para tomar foto y analizarla
    
    if (Serial.available()>0){
      char comando = Serial.read(); //recibe la letra para activar activar el clasificador y posicionarlo en su deposito correspondiente

      switch(comando){
        case 'p':
             {
              //azul verde se enciende y apaga
             digitalWrite(ledazul, HIGH);
             delay(2000);
             digitalWrite(ledazul, LOW);
             }
             {
             //CLASIFICARDOR A PAPEL azul
             //el clasificador se mantine en su posición 
             motor1.step(0); 
             }
             //Abrir tapa para que la basura sea liberada y depositada
             //servo
             servoMotor.write(180);
             delay(5000);  
             //Tapadera se vuelve a cerrar
             servoMotor.write(0);
             break;
             
         case 'O':
              {
              //led verde se enciende y apaga
              digitalWrite(ledverde, HIGH);
              delay(2000);
              digitalWrite(ledverde, LOW);
              }
              {
              //CLASIFICADOR A ORGANICOS verde
              motor1.step(512); //cantidad de pasos adelante
              }
              //Abrir tapa para que la basura sea liberada y depositada
              // Tapadera
              motor1.step(0);
              servoMotor.write(180);//Servo
              delay(7000);

              // Tapadera se vuelve a cerrar
              motor1.step(0);
              servoMotor.write(125);//Servo
              delay(7000);
             
              {
              //REGRESA EL CLASIFICADOR A LA POSICIÓN INICIAL
              motor1.step(-512);
              }
                       
              break;
              
          case 'P':
              {
              // led anaranjado se enciende y apaga
              digitalWrite(lednaranja, HIGH);
              delay(2000);
              digitalWrite(lednaranja, LOW);
              }
              {
               //CLASIFICADOR A PLASTICO amarillo
               motor1.step(-1024); //cantidad de pasos adelante
               }
               //Abrir tapa para que la basura sea liberada y depositada
               // Servo
               motor1.step(0);
               servoMotor.write(180);//servo
               // Esperamos 1 segundo
               delay(12000);
  
               // Tapadera se vuelve a cerrar
               motor1.step(0);
               servoMotor.write(125);//servo
               delay(7000);
               
                {
               //REGRESA EL CLASIFICADOR A LA POSICIÓN INICIAL
               motor1.step(1024); 
                }
                
                
                break;
                
           case 'M':
                {
                // led blanco se enciende y apaga
                digitalWrite(ledblanco, HIGH);
                delay(2000);
                digitalWrite(ledblanco, LOW);
                }
                {
                //CLASIFICADOR A METAL gris
                motor1.step(-512); //cantidad de pasos adelante
                }
                //Abrir tapa para que la basura sea liberada y depositada
                //Tapadera
                motor1.step(0);
                servoMotor.write(180);
                //servo
                 
                delay(6000);
                  
                //Tapadera  se vuelve a cerrar
                motor1.step(0);
                servoMotor.write(125);
                //servo
                    
                delay(6000);
                {
                //REGRESA EL CLASIFICADOR A LA POSICIÓN INICIAL
                motor1.step(512); 
                }
                
                break;

            case 'V':
                //si lo indentificado no es basura enciende led rojo y no habre la tapadera
                digitalWrite(ledrojo, HIGH);
                delay(5000);
                digitalWrite(ledrojo, LOW);
                break;
           }
        }
      else{}
    }
    else{} 
}
