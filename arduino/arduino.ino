// Sole purpose is ADC
int sensorPin = A0;
int sensorValue;

void setup() {
 Serial.begin(9600);
}

void loop() {
 sensorValue = analogRead(sensorPin);
 float percentage = (sensorValue/1024)*100; // % moisture
 Serial.println(percentage);
 delay(18000000); //every 30 minutes
}
