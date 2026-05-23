🌱 Smart Irrigation System using IoT, GSM & Machine Learning (SVM)
📌 Overview

The Smart Irrigation System is an intelligent solution designed to automate and optimize irrigation using IoT, GSM communication, and machine learning (Support Vector Machine - SVM).

The system monitors soil moisture, temperature, and humidity in real time, predicts irrigation needs, and transmits data remotely via GSM—making it ideal for deployment in areas with limited or no Wi-Fi connectivity.

🚀 Features
 Temperature and humidity monitoring (DHT11)
 Soil moisture sensing for accurate irrigation decisions
 GSM-based remote communication (SMS/GPRS)
 Machine learning (SVM) for smart irrigation prediction
 Automated water pump control via relay
 Remote alerts and control via SMS
 Durable 3D-printed enclosure
 Efficient and scalable system design
 System Architecture
Components:
ESP32 Microcontroller – central controller
DHT11 Sensor – temperature & humidity
Soil Moisture Sensor – measures soil water content
GSM Module (SIM800L / SIM900) – remote communication
Relay Module – controls water pump
Water Pump – irrigation actuator
Cloud/Server (optional) – data storage & ML hosting
3D Printed Enclosure – protects hardware
Workflow:
Soil moisture sensor measures water content in soil.
DHT11 captures temperature and humidity.
ESP32 processes all sensor data.
SVM model predicts whether irrigation is required.
Relay switches the water pump ON/OFF.
GSM module:
Sends system data via SMS or GPRS
Receives remote commands (optional)
Data is logged for monitoring and model improvement.
🛠️ Hardware Components
ESP32 Development Board
DHT11 Temperature & Humidity Sensor
Soil Moisture Sensor (capacitive recommended)
GSM Module (SIM800L / SIM900)
SIM Card (active plan required)
Relay Module
Water Pump
Power Supply (stable, especially for GSM module)
Jumper Wires
3D Printed Enclosure
💻 Software & Technologies
Programming Languages: Arduino C++ / Python
Machine Learning: Support Vector Machine (SVM)
Communication Protocols:
GSM (SMS, GPRS)
HTTP/MQTT (via GPRS for cloud integration)
Libraries:
DHT sensor library
TinyGSM
SoftwareSerial / Hardware Serial
ArduinoJson
scikit-learn (for training SVM model)
⚙️ Installation & Setup
1. Hardware Setup
Connect DHT11 to ESP32 GPIO
Connect soil moisture sensor to analog pin (GPIO)
Connect GSM module:
TX → RX (ESP32)
RX → TX (ESP32)
Ensure proper voltage regulation
Connect relay module to ESP32
Attach water pump to relay
Insert SIM card into GSM module
Power the system
2. Software Setup
Install Arduino IDE / PlatformIO
Install required libraries
Configure GSM settings (APN, SIM)
Upload firmware to ESP32
3. Machine Learning Model
Collect dataset:
Temperature
Humidity
Soil Moisture
Irrigation status (ON/OFF)
Train SVM model using scikit-learn
Export trained model
Deploy:
Locally (simplified logic on ESP32), or
Remotely (server queried via GSM GPRS)
📊 Machine Learning Model (SVM)
Input Features:
Temperature
Humidity
Soil Moisture
Output:
Irrigation Decision (ON/OFF)

The SVM model improves irrigation efficiency by combining environmental and soil data for more accurate predictions.

📡 GSM Communication

The GSM module enables:

📩 SMS alerts:
Soil moisture levels
Temperature & humidity
Pump status
🌐 GPRS data upload to cloud dashboards
📲 Remote commands:
Turn irrigation ON/OFF
Request system status
📷 Project Design

The 3D-printed enclosure ensures:

Protection against dust and moisture
Organized component placement
Field-ready deployment
🔍 Future Improvements
Add pH and nutrient sensors
Integrate weather forecast APIs
Solar-powered system
Mobile/web dashboard
Use advanced ML models (e.g., Random Forest, Deep Learning)
Multi-zone irrigation control
🤝 Contributions

Contributions and improvements are welcome. Feel free to fork the repository and submit a pull request.
