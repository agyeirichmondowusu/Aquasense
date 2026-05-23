from fastapi import FastAPI, Request
import uvicorn
import joblib
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

model = joblib.load("irrigation_svm_model.pkl")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)


# New sample (temperature, humidity, moisture)

temperature = 0
humidity = 0
soil_moisture = 0

# sample = pd.DataFrame([{
#     "temperature": temperature,
#     "humidity": humidity,
#     "moisture": soil_moisture
# }])
sample_data = {
    "temperature": temperature,
    "humidity": humidity,
    "moisture": soil_moisture
}


@app.post('/predict')
async def get_humid(value: Request):
    global humidity, temperature, soil_moisture
    data = await value.json()

    temperature = data.get('temperature')
    humidity = data.get('humidity')
    soil_moisture = data.get('moisture')

    if None in (temperature, humidity, soil_moisture):
        return {"label": "Missing fields", "received": data}
    
    sample = pd.DataFrame([{
        "temperature": temperature,
        "humidity": humidity,
        "moisture": soil_moisture
    }])

    print(f'Temperature: {temperature}')
    print(f'Humidity: {humidity}')
    print(f'Soil moisture: {soil_moisture}')

    # sample["temperature"] = temperature
    # sample["humidity"] = humidity
    # sample["moisture"] = soil_moisture

    # Predict
    prediction = model.predict(sample)[0]
    print("prediction", prediction)

    return {"label": bool(prediction)}


@app.post('/update')
async def update(request: Request):
    data = await request.json()
    temperature = data.get("temperature")
    humidity = data.get("humidity")
    soil_moisture = data.get("moisture")

    sample_data["temperature"] = temperature
    sample_data["humidity"] = humidity
    sample_data["moisture"] = soil_moisture
    return {"response": "updated"}


@app.get('/stream')
async def stream():
    return {"data": sample_data}
    



if __name__=='__main__':
    uvicorn.run(app, host="0.0.0.0", port=5400)




