// Sole purpose is ADC
int sensorPin = A0;
int sensorValue;

void setup() {
 Serial.begin(9600);
}

void loop() {
 sensorValue = analogRead(sensorPin);
 Serial.println(sensorValue);
 delay(1000); // every second for the sake of testing
}
