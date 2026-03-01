#include <Arduino.h>

#define VRX_PIN 25
#define VRY_PIN 26

int servoX = 0;
int servoY = 0;

void setup()
{
    Serial.begin(9600);
}

void loop()
{

    servoX = analogRead(VRX_PIN);
    servoY = analogRead(VRY_PIN);

    Serial.print("\nx: ");
    Serial.print(servoX);
    Serial.print(" y: ");
    Serial.print(servoY);

    delay(50);
}
