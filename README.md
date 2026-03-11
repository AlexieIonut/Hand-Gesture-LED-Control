# AI Hand Gesture Control for Arduino

This project uses Computer Vision to detect hand gestures and control physical hardware. By leveraging **MediaPipe** for hand landmark detection and **PyFirmata2** for Arduino communication, you can control 5 LEDs in real-time with your fingers.

##Features
- **Real-time Detection:** High-speed hand tracking using MediaPipe's Tasks API.
- **Orientation Awareness:** The system distinguishes between the palm facing the camera or the back of the hand.
- **Multi-LED Control:** Maps each finger to a specific Arduino digital pin.
- **Hardware Abstraction:** Uses the Firmata protocol to control Arduino directly from Python without constant re-uploading of C++ code.

##Hardware Requirements
- **Microcontroller:** Arduino Uno / Nano / Mega.
- **Components:** 5x LEDs, 5x 220Ω Resistors, Jumper wires.
- **Pin Mapping:**
  - Thumb: Pin 2
  - Index: Pin 3
  - Middle: Pin 4
  - Ring: Pin 5
  - Pinky: Pin 6

##Software Setup

### 1. Arduino Setup
Before running the Python script, you must upload the **StandardFirmata** sketch to your Arduino:
1. Open Arduino IDE.
2. Go to `File` > `Examples` > `Firmata` > `StandardFirmata`.
3. Select your board and port, then click **Upload**.

### 2. Python Environment
It is recommended to use a virtual environment:
```bash
# Create a virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
