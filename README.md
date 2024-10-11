# Cough-Strength-Measuring-device-using-ML-DL-and-Multisensory-Approach-

**Overview**
This project aims to develop a Cough Strength Measuring Device that leverages machine learning and a multisensory approach to objectively measure cough strength. It addresses the limitations of existing subjective methods, providing more accurate and consistent results, thus improving the diagnosis and treatment of patients with chronic cough.

**Features**
Objective Cough Strength Measurement: Combines data from pressure sensors and microphones to evaluate the force and sound of coughs.

Multisensory Approach: Utilizes sensor data to ensure comprehensive results, reducing the reliance on traditional methods.

Real-time Monitoring: Data is collected and stored for remote diagnosis, with cloud integration for real-time monitoring.

User-Friendly Interface: The device comes with an intuitive interface that allows users to input personal data such as age, height, and weight, and receive accurate results.

AI/ML Integration: The system uses machine learning algorithms to predict cough severity based on collected data.

**Components**

**Hardware**

Pressure Sensor (GY-63): Measures the force of the cough.

MEMS Microphone (INMP-441): Captures the sound of the cough to extract features like amplitude and frequency.

ESP-32: For data collection and communication with the software.

SD Card Module: For local data storage.

**Software**
Machine Learning Libraries: Scikit-learn, TensorFlow, PyTorch, etc., for model training and testing.

Flutter: For mobile app development.

Arduino IDE: For hardware testing and sensor calibration.

**System Architecture**

Data Collection: Sensors capture cough strength and sound data, which is then cleaned, organized, and processed.

Feature Extraction: Key features like pressure, frequency, and amplitude are extracted from the raw data.

Model Training and Evaluation: The extracted features are used to train a classification model that predicts cough severity (normal, moderate, severe).

Real-time Predictions: The trained model is integrated into the device for real-time cough severity predictions.

**How to Use**

Input Personal Data: The user enters basic information such as age, weight, and height.

Perform Cough Test: The user coughs into the device, and sensors record the cough data.

View Results: The device processes the data and displays the severity score on the interface.

Cloud Storage: Data is uploaded to the cloud for remote analysis by healthcare providers.

