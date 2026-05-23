import joblib
import pandas as pd

# Load trained model
model = joblib.load("irrigation_svm_model.pkl")

# New sample (temperature, humidity, moisture)
sample = pd.DataFrame([{
    "temperature": 90,
    "humidity": 10,
    "moisture": 20.5
}])

# Predict
prediction = model.predict(sample)[0]

print("Irrigation needed:", bool(prediction))



# For these exact reasons, tune the initial dataset to meet the requirements of the svm model in an analog farming environment. Check which conditions are most likely to need watering

# In determining soil type, are there arduino sensors for doing that?

# Make soil moisture the dominant driver, with temperature and humidity acting as modifiers

# Re-generate the dataset using analog (soft, noisy) farming conditions

# Make soil moisture the dominant driver, with temperature and humidity acting as modifiers

# Ensure class overlap near decision boundaries (so SVM actually learns, not memorizes)

# Balance TRUE/FALSE for stability

# Deliver a downloadable CSV ready for high-accuracy SVM training