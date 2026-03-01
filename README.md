# THUNDER_POINTER

THUNDER_POINTER is a joystick-controlled dual-servo system designed for the ESP32. It provides smooth two-axis movement and can optionally control a laser diode.

## Requirements:

* ESP32 ×1
* Analog joystick ×1
* 180° servos ×2
* Laser diode (optional) ×1
* External power supply (recommended)

## The microcontroler

The project was originally prototyped on a Raspberry Pi, but the final version targets the ESP32 due to better performance, lower latency, and more stable PWM control using C++.

ESP32 is strongly recommended.

## IMPORTANT!!! - Raspberry Pi Notice

The Raspberry Pi .py files are prototype-only and not finalized. They may be incomplete or unstable and will not be maintained. Use them at your own risk.
