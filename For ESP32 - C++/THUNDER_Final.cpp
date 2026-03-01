#include <Arduino.h>
#include <ESP32Servo.h>

#define VRX_PIN 25
#define VRY_PIN 26

Servo xServo;
Servo yServo;

int xPin = 18;
int yPin = 19;
int ValueX = 0;
int ValueY = 0;

void setup()
{
    Serial.begin(9600);

    xServo.attach(xPin);
    yServo.attach(yPin);

    xServo.write(90);
    yServo.write(90);
}

void loop()
{
    ValueX = analogRead(VRX_PIN);
    ValueY = analogRead(VRY_PIN);

    Serial.print("\nx: ");
    Serial.print(ValueX);
    Serial.print(" y: ");
    Serial.print(ValueY);

    xServo.write(map(ValueX, 0, 4095, 0, 180));
    yServo.write(map(ValueY, 0, 4095, 0, 180));

    delay(50);
}
