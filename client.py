import requests
import time
import random
url = "http://127.0.0.1:5400/stream"
url = "https://aquasense-00z1.onrender.com/stream"
temperature = 0
humidity = 0
soil_moisture = 0



while True:
    # temperature = round(random.gauss(75, 2), 2)
    # humidity = round(random.gauss(20, 1.5), 2)
    # soil_moisture = round(random.gauss(35, 3), 2)
    
    data = {
    "temperature": round(random.gauss(75, 2), 2),
    "humidity": round(random.gauss(20, 1.5), 2),
    "moisture": round(random.gauss(35, 3), 2)
    }
    # data = {
    #     "temperature": temperature,
    #     "humidity": humidity,
    #     "moisture": soil_moisture
    # }
    # response = requests.post(url, json=data)
    response = requests.get(url=url)
    if response.ok:
        data = response.json()
        print("Request sent")
        # print(repr(data.text))
        print("status: ", data.get("data"))

    else:
        print("Request failed")

    time.sleep(1)