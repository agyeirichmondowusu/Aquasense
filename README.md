🌱 Smart Irrigation System using IoT & Machine Learning (SVM)
Overview

The Smart Irrigation System is an intelligent, IoT-enabled solution designed to automate and optimize agricultural watering processes. By leveraging real-time environmental data and machine learning (Support Vector Machine - SVM), the system monitors key parameters and predicts when irrigation is necessary, ensuring efficient water usage and improved crop health.

Features
Real-time temperature and humidity monitoring using DHT11
IoT-based remote monitoring and control
Machine learning (SVM) for irrigation prediction
Automated water pump control via relay
Compact 3D-printed enclosure for hardware protection
⚡ Low-power and cost-effective design
 System Architecture

The system consists of:

ESP32 Microcontroller – central processing unit with Wi-Fi capability
DHT11 Sensor – collects temperature and humidity data
Relay Module – controls the water pump (ON/OFF)
Water Pump – performs irrigation
Cloud/Server (optional) – stores data and hosts ML model
3D Printed Enclosure – houses and protects components
Workflow:
DHT11 collects environmental data (temperature & humidity).
ESP32 processes and transmits data.
The SVM model predicts whether irrigation is needed.
Relay is triggered to turn the water pump ON/OFF accordingly.
Data can be logged for monitoring and future analysis.

 Hardware Components
ESP32 Development Board
DHT11 Temperature & Humidity Sensor
Relay Module (5V/3.3V compatible)
Water Pump
Power Supply
Connecting Wires
3D Printed Enclosure
 Software & Technologies
Programming Language: Python / Arduino C++
Machine Learning: Support Vector Machine (SVM)
IoT Platform: MQTT / HTTP (depending on implementation)
Libraries:
DHT sensor library
WiFi.h
scikit-learn (for SVM model training)
ArduinoJson (optional)

GSM Communication

The GSM module enables:

 Sending SMS alerts:
Current temperature & humidity
Irrigation status
 GPRS data transmission to cloud platforms
 Receiving remote commands:
Turn pump ON/OFF
Request system status

Installation & Setup
1. Hardware Setup
Connect DHT11 to ESP32 (GPIO pin)
Connect relay module to ESP32
Attach water pump to relay
Power the ESP32 and system
2. Software Setup
Install Arduino IDE / PlatformIO
Install required libraries
Upload code to ESP32
3. Machine Learning Model
Collect dataset (temperature, humidity, irrigation status)
Train SVM model using scikit-learn
Export model (e.g., .pkl file)
Deploy model locally or integrate into cloud system

Machine Learning Model (SVM)

The SVM model is used to:

Analyze environmental conditions
Predict whether irrigation is required
Input Features:
Temperature
Humidity
Output:
Irrigation Decision (ON/OFF)

IoT Integration
ESP32 sends sensor data via Wi-Fi
Data can be visualized on a dashboard (e.g., ThingsBoard, Blynk)
Remote monitoring and control supported
 Project Design
Custom 3D-printed enclosure ensures:
Protection from environmental factors
Compact and portable design
Easy installation in farm environments
 Future Improvements
Add soil moisture sensor for better accuracy
Integrate weather forecast APIs
Use more advanced ML models (e.g., Random Forest, Neural Networks)
Mobile app for real-time monitoring
Solar-powered system for sustainability
 Contributions

Contributions, suggestions, and improvements are welcome. Feel free to fork this repository and submit a pull request.
