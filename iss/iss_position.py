import requests
import time
url_iss = "http://api.open-notify.org/iss-now.json"
while True:
    response = requests.get(url_iss)
    data_original = response.json()
    data = data_original['iss_position']
    result = f"{time.ctime()}:\nlongitude: {data['longitude']}\nlatitude: {data['latitude']}\n"

    with open(f'iss.csv', 'a') as file:
        file.write(result)
    time.sleep(5)
