# Traffic-Light-Simulation

This project includes both hardware (Arduino) and software (Python) simulations of a traffic light.

## Hardware Simulation (Arduino)

### Hardware Requirements
- Arduino board (e.g., Arduino Uno)
- 3 LEDs (Red, Yellow, Green)
- 3 resistors (220Ω each)
- Jumper wires
- Breadboard

### Circuit Setup
- Connect Red LED to pin 2
- Connect Yellow LED to pin 3
- Connect Green LED to pin 4
- Use resistors in series with each LED to limit current

### How to Build and Upload
1. Install the Arduino IDE from https://www.arduino.cc/en/software
2. Open the `Traffic_Light_Simulation.ino` file in the Arduino IDE
3. Select your Arduino board type (Tools > Board)
4. Select the correct port (Tools > Port)
5. Click the Upload button (right arrow icon) to compile and upload the code to your Arduino board

## Software Simulation (Python)

### Requirements
- Python 3.x

### How to Run
1. Run `python traffic_light_simulation.py` in the terminal
2. The simulation will print the current light color every cycle

## How It Works
The simulation cycles through the traffic light sequence:
- Red light for 3 seconds
- Yellow light for 1 second
- Green light for 3 seconds
- Repeat